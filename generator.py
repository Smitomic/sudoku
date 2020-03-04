from solver import *
from random import shuffle, randint


def solver_modified(grid):
    empty = find_next(grid)
    if not empty:
        return True

    numbers = [i for i in range(1, 10)]
    shuffle(numbers)
    for i in numbers:
        if check_placement(grid, empty, i):
            grid[empty[0]][empty[1]] = i

            if solver_modified(grid):
                return True
            else:
                grid[empty[0]][empty[1]] = 0
    return False


def is_solved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True


count = 0


def solver_counter(grid):
    # for checking if it has only one solution
    global count
    empty = find_next(grid)
    if not empty:
        return

    for i in range(1, 10):
        if check_placement(grid, empty, i):
            grid[empty[0]][empty[1]] = i

            solver_counter(grid)
            if is_solved(grid):
                count += 1
            grid[empty[0]][empty[1]] = 0


def sudoku_grid():
    global count
    # first, we generate empty grid
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # then we fill it in with solver modified by random number insertion
    solver_modified(grid)

    # lastly, start removing certain numbers while checking if the sudoku
    # is still solvable with every removal, we limit the number of removals by
    # giving a specific number of failed tries which should translate
    # into difficulty as well
    tries = 5
    while tries > 0:
        # finding a non-empty square
        x = randint(0, 8)
        y = randint(0, 8)
        while grid[x][y] == 0:
            x = randint(0, 8)
            y = randint(0, 8)

        # we save the original number, then remove it from board and check
        # if it is solvable
        original = grid[x][y]
        grid[x][y] = 0
        grid_copy = [x[:] for x in grid]
        solver_counter(grid_copy)
        if count != 1:
            grid[x][y] = original
            tries -= 1
        count = 0
    return grid
