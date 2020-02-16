import numpy as np
from sudoku.solve import Solve
from sudoku.structures import GridType

class Grid:
    def __init__(self):
        """ Initialize the grid with zeros """
        self.active: GridType = np.zeros((9, 9))

    
    def _update(self, grid: GridType) -> None:
        """ Update the active grid """
        self.active = grid


    def populate(self, grid: GridType) -> None:
        """ Populate the grid with given input """
        self._update(grid)


    def solve(self) -> None:
        """ Solve active grid """
        grid = Solve.solve(self.active)
        self._update(grid)