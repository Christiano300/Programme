def print_sudoku(sudoku: list) -> None:
    print("-" * 37)
    for i, row in enumerate(sudoku):
        print("| ", end='')
        for cell in row:
            print(cell if cell else " ", "| ", end='', sep=' ')
        print()
        print("-" * 37)

