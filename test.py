import numpy as np
from sudoku.grid import Grid

def main():
    board = np.array([
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 8, 0, 0, 0, 7, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 7, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 4, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 3],
        [0, 9, 0, 4, 0, 0, 0, 7, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0]
    ])

    # Initialize an empty grid object
    grid = Grid()
    
    # Populate grid with known board (eventually read layout from img)
    grid.populate(board)
    #print(grid.active)

    # Solve current board
    grid.solve()
    #print(grid.active)

if __name__ == "__main__":
    main()