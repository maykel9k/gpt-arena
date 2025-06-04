from __future__ import annotations

import random
import time
from typing import List


class GameOfLife:
    def __init__(self, rows: int, cols: int, randomize: bool = True) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = self._create_grid(randomize)

    def _create_grid(self, randomize: bool) -> List[List[int]]:
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def step(self) -> None:
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                alive = self.grid[r][c] == 1
                neighbors = self._count_neighbors(r, c)
                if alive and neighbors in (2, 3):
                    new_grid[r][c] = 1
                elif not alive and neighbors == 3:
                    new_grid[r][c] = 1
        self.grid = new_grid

    def _count_neighbors(self, row: int, col: int) -> int:
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r][c]
        return count

    def display(self) -> None:
        lines = []
        for row in self.grid:
            lines.append(''.join('█' if cell else ' ' for cell in row))
        print('\n'.join(lines))


if __name__ == "__main__":
    game = GameOfLife(rows=20, cols=40)
    try:
        while True:
            game.display()
            game.step()
            time.sleep(0.2)
            print("\x1b[H\x1b[J", end="")  # Clear screen
    except KeyboardInterrupt:
        pass
