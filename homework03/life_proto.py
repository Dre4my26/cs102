"importing libraries"
# pylint: disable=no-member, consider-using-enumerate

from copy import deepcopy
from itertools import product
from typing import List, Tuple
from pygame.locals import *

import random
import pygame

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    """
    implementing main funcs
    """

    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        """
        pylint says I should add docstrings
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        self.grid: Grid = []

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for width in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color(
                    "black"), (width, 0), (width, self.height)
            )
        for height in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color(
                    "black"), (0, height), (self.width, height)
            )

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Отрисовка списка клеток
            self.draw_grid()
            self.draw_lines()
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if randomize == True:

            grid = [
                [random.randint(0, 1) for j in range(self.cell_height)]
                for i in range(self.cell_width)
            ]
        else:
            grid = [
                [0 for j in range(self.cell_height)] for i in range(self.cell_width)
            ]
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                cell_color = pygame.Color(
                    "green") if self.grid[i][j] else pygame.Color("white")
                rect = pygame.Rect(
                    j * self.cell_size,
                    i * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, cell_color, rect)

    def _is_valid_cell(self, candidate: Cell) -> bool:
        return 0 <= candidate[0] < len(self.grid) and 0 <= candidate[1] < len(
            self.grid[0]
        )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """

        neighbours = []

        deltas = [-1, 0, 1]
        for cord_dx, cord_dy in product(deltas, deltas):
            if (cord_dx, cord_dy) == (0, 0):
                continue

            row, col = cell[0] + cord_dy, cell[1] + cord_dx
            if self._is_valid_cell((row, col)):
                is_alive = self.grid[row][col]
                neighbours.append(is_alive)

        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        out = deepcopy(self.grid)

        for i in range(len(out)):
            for j in range(len(out[i])):
                alive_neighbours = sum(self.get_neighbours((i, j)))

                if self.grid[i][j]:
                    out[i][j] = int(2 <= alive_neighbours <= 3)
                elif alive_neighbours == 3:
                    out[i][j] = i

        return out


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()
    game.run().draw_grid()
