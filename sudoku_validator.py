def is_valid_sudoku(board, custom_zones):
    def is_valid_group(group):
        digits = [cell for cell in group if cell != '.']
        return len(set(digits)) == len(digits)

    for row in board:
        if not is_valid_group(row):
            return False

    for col in zip(*board):
        if not is_valid_group(col):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = [board[r][c] for r in range(box_row, box_row + 3)
                                   for c in range(box_col, box_col + 3)]
            if not is_valid_group(block):
                return False

    for zone in custom_zones:
        zone_digits = [board[r][c] for r, c in zone if board[r][c] != '.']
        if len(set(zone_digits)) != len(zone_digits):
            return False

    return True


def test_sudoku_validator():
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    valid_custom_zones = [
        [(0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (2, 2), (2, 7), (3, 0)],
        [(3, 4), (3, 8), (4, 0), (4, 3), (4, 5), (5, 0), (5, 4), (5, 8), (6, 1)],
        [(6, 6), (6, 7), (7, 3), (7, 4), (7, 5), (8, 4), (8, 7), (8, 8), (3, 3)]
    ]

    invalid_custom_zones = [
        [(0, 0), (0, 1), (0, 4), (1, 0), (1, 3), (1, 4), (2, 2), (2, 7), (0, 0)]
    ]

    print(is_valid_sudoku(valid_board, valid_custom_zones))
    print(is_valid_sudoku(valid_board, invalid_custom_zones))

    invalid_board = [row[:] for row in valid_board]
    invalid_board[0][2] = "5"
    print(is_valid_sudoku(invalid_board, valid_custom_zones))

    invalid_board_2 = [row[:] for row in valid_board]
    invalid_board_2[1][0] = "6"
    print(is_valid_sudoku(invalid_board_2, valid_custom_zones))

    invalid_board_3 = [row[:] for row in valid_board]
    invalid_board_3[2][0] = "8"
    print(is_valid_sudoku(invalid_board_3, valid_custom_zones))


if __name__ == "__main__":
    test_sudoku_validator()
