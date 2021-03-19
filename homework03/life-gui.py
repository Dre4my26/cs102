# pylint: disable=no-member ,missing-class-docstring, unused-wildcard-import, missing-module-docstring, missing-function-docstring

import pathlib
import pygame  # type: ignore
from pygame.locals import *  # type: ignore
import life
from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.speed = speed

    def draw_lines(self) -> None:
        for x_c in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(
                "black"), (x_c, 0), (x_c, self.height))

        for y_c in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color(
                "black"), (0, y_c), (self.width, y_c))

    def draw_grid(self) -> None:
        for i in range(len(self.life.curr_generation)):
            for j in range(len(self.life.curr_generation[i])):
                cell_color = (
                    pygame.Color("green")
                    if self.life.curr_generation[i][j]
                    else pygame.Color("white")
                )
                rect = pygame.Rect(
                    j * self.cell_size,
                    i * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, cell_color, rect)

    def change_state(self, cell: life.Cell) -> None:
        cell_x = cell[0] // self.cell_size
        cell_y = cell[1] // self.cell_size
        if self.life.curr_generation[cell_x][cell_y]:
            self.life.curr_generation[cell_x][cell_y] = 0
        else:
            self.life.curr_generation[cell_x][cell_y] = 1

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        self.life.curr_generation = self.life.create_grid(randomize=True)

        running = True
        pause = False
        while running:
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (
                        y_c,
                        x_c,
                    ) = (
                        pygame.mouse.get_pos()
                    )  # inverted due to graphics having a weird coordinate system
                    self.change_state((x_c, y_c))
                    self.draw_grid()
                    self.draw_lines()
                    pygame.display.flip()
                    clock.tick(self.speed)
                    continue
                elif event.type == pygame.KEYDOWN:  # get event
                    if event.key == pygame.K_SPACE:  # check pause key
                        if pause:
                            pause = False
                        else:
                            pause = True

            if pause:  # actually pause the game
                continue

            # Выполнение одного шага игры (обновление состояния ячеек)
            if self.life.is_changing and not self.life.is_max_generations_exceeded:
                self.life.step()
                pygame.display.flip()
            else:
                running = False

            clock.tick(self.speed)
        pygame.quit()


def main():
    game = GameOfLife(size=(48, 64))
    app = GUI(game)
    app.run()


if __name__ == "__main__":
    main()
