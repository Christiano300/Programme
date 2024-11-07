def print_sudoku(sudoku: list) -> None:
    print("-" * 37)
    for i, row in enumerate(sudoku):
        print("| ", end='')
        for cell in row:
            print(cell if cell else " ", "| ", end='', sep=' ')
        print()
        print("-" * 37)

sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
          [2, 3, 4, 5, 6, 7, 8, 9, 1],
          [3, 4, 5, 6, 7, 8, 9, 1, 2],
          [4, 5, 6, 7, 8, 9, 1, 2, 3],
          [5, 6, 7, 8, 9, 1, 2, 3, 4],
          [6, 7, 8, 9, 1, 2, 3, 4, 5],
          [7, 8, 9, 1, 2, 3, 4, 5, 6],
          [8, 9, 1, 2, 3, 4, 5, 6, 7],
          [9, 1, 2, 3, 4, 5, 6, 7, 8]]

print_sudoku(sudoku)