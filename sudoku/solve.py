import numpy as np
from sudoku.structures import GridType, Segments

class Solve:
    @staticmethod
    def solve(grid: GridType) -> None:
        """ Solve the input grid """
        segments = Solve.segment(grid)
        return grid 


    @staticmethod
    def segment(grid: GridType) -> Segments:
        """ Segment input grid into rows, columns, and blocks """
        rows = grid[:,]
        columns = grid.T[:,]
        blocks = np.array([
            np.concatenate(grid[0:3, 0:3]),
            np.concatenate(grid[0:3, 3:6]),
            np.concatenate(grid[0:3, 6:]),
            np.concatenate(grid[3:6, 0:4]),
            np.concatenate(grid[3:6, 3:6]),
            np.concatenate(grid[3:6, 6:]),
            np.concatenate(grid[6:, 0:4]),
            np.concatenate(grid[6:, 3:6]),
            np.concatenate(grid[6:, 6:]),
        ])
        return Segments(rows=rows, columns=columns, blocks=blocks)


