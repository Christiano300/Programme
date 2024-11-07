from typing import Generator, Union

boards = {}

def check_for_winner(grid: list) -> Union[str, None]:
    for i in grid:
        if i[0] != " " and i[0] == i[1] == i[2]:
            return i[0]
    for i in range(3):
        if grid[0][i] != " " and grid[0][i] == grid[1][i] == grid[2][i]:
            return grid[0][i]
    if grid[0][0] != " " and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] != " " and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]
    return None

def find_next_free(grid: list) -> Generator[tuple[int, int], None, None]:
    for x in range(3):
        for y in range(3):
            if grid[x][y] == " ":
                yield x, y

def board_to_string(grid: list) -> str:
    return "".join("".join(row) for row in grid)

def f(board: list, player: str):
    for x, y in find_next_free(board):
        board[x][y] = player
        board_str = board_to_string(board)
        full = all(all(i != " " for i in row) for row in board)
        if not (full or check_for_winner(board)):
            boards[board_str] = boards.get(board_str, 0) + 1
            f(board, "X" if player == "O" else "O")
        board[x][y] = " "


f([[" " for _ in range(3)] for _ in range(3)], "X")

print(len(boards))
print(*boards.items(), sep="\n", file=open("ignfiles/tictactoe_combs.txt", "w"))