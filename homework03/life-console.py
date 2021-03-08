# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.rows = len(self.life.curr_generation)
        self.cols = len(self.life.curr_generation[0])

    def draw_borders(self, screen) -> None:
        screen.border()

    def draw_grid(self, screen) -> None:
        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                symbol = "*" if self.life.curr_generation[i][j] else " "
                screen.addch(i, j, symbol)

    def run(self) -> None:
        term = curses.initscr()
        screen = term.derwin(self.rows, self.cols, 0, 0)
        self.draw_borders(screen)

        try:
            while (
                self.life.is_changing
                or not self.life.is_max_generations_exceeded
            ):
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()
                self.life.step()
        finally:
            curses.endwin()


def main():
    game = GameOfLife(size=(32, 80))
    app = Console(game)
    app.run()


if __name__ == "__main__":
    main()
