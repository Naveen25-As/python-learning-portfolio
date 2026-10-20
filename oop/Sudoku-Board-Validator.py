# Sudoku Board Validator.

def valid_group(group):
    return sorted(group) == list(range(1, 10))


def validate_sudoku(board):
    for row in board:
        if not valid_group(row):
            return False

    for col in range(9):
        column = [board[row][col] for row in range(9)]

        if not valid_group(column):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []

            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    box.append(board[row][col])

            if not valid_group(box):
                return False

    return True


board = []

print("Enter 9 rows, each containing 9 digits separated by spaces.")

try:
    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        if len(row) != 9 or any(n < 1 or n > 9 for n in row):
            raise ValueError("Each row must contain 9 digits from 1 to 9.")

        board.append(row)

    if validate_sudoku(board):
        print("Valid completed Sudoku board!")
    else:
        print("Invalid Sudoku board.")

except ValueError as error:
    print("Invalid input:", error)
