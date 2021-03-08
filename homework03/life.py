# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import json
import pathlib
import random
from copy import deepcopy
from itertools import product
from typing import List, Optional, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: float = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        return [
            [random.randint(0, 1) if randomize else 0 for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def _is_valid_cell(self, candidate: Cell) -> bool:
        return 0 <= candidate[0] < self.rows and 0 <= candidate[1] < self.cols

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []

        deltas = [-1, 0, 1]
        for d_x, d_y in product(deltas, deltas):
            if (d_x, d_y) == (0, 0):
                continue

            row, col = cell[0] + d_y, cell[1] + d_x
            if self._is_valid_cell((row, col)):
                is_alive = self.curr_generation[row][col]
                neighbours.append(is_alive)

        return neighbours

    def get_next_generation(self) -> Grid:
        out = deepcopy(self.curr_generation)

        for i in range(len(out)):
            for j in range(len(out[i])):
                alive_neighbours = sum(self.get_neighbours((i, j)))

                if self.curr_generation[i][j]:
                    out[i][j] = int(2 <= alive_neighbours <= 3)
                elif alive_neighbours == 3:
                    out[i][j] = 1

        return out

    def step(self) -> None:
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        with open(filename, "r") as f:
            curr_generation = json.load(f)

        size = len(curr_generation), len(curr_generation[0])
        game = GameOfLife(size=size, randomize=False)
        game.curr_generation = curr_generation

        return game

    def save(self, filename: pathlib.Path) -> None:
        with open(filename, "w") as f:
            json.dump(self.curr_generation, fp=f)


def main():
    filename = "generation_{}.txt"

    def gen_path(step):
        return pathlib.Path(filename.format(step)).resolve()

    # New game
    game = GameOfLife(size=(48, 64))
    game.step()
    game.save(gen_path(0))

    # Game from save
    game = GameOfLife.from_file(gen_path(0))
    game.step()
    game.save(gen_path(1))


if __name__ == "__main__":
    main()