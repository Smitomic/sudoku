def check_placement(grid, coord, num):
    # row
    for i in range(len(grid)):
        if grid[coord[0]][i] == num:
            return False

    # column
    for i in range(len(grid)):
        if grid[i][coord[1]] == num:
            return False

    # box
    x = coord[0] // 3
    y = coord[1] // 3
    for i in range(x*3, x*3+3):
        for j in range(y*3, y*3+3):
            if grid[i][j] == num:
                return False

    return True


def draw_board(grid):
    for i in range(9):
        if i % 3 == 0:
            print("- " * 13)
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print("|")
    print("- " * 13)


# finds next empty space to fill in
def find_next(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j


def solving_algo(grid):
    empty = find_next(grid)
    if not empty:
        return True

    for i in range(1, 10):
        if check_placement(grid, empty, i):
            grid[empty[0]][empty[1]] = i

            # backtracking through using a recursion in if statement -
            # if something fails it goes depth up and tries to go deeper again
            # with different number
            if solving_algo(grid):
                return True
            else:
                grid[empty[0]][empty[1]] = 0
    return False


# draw_board(board)
# print(solving_algo(board))
# draw_board(board)
