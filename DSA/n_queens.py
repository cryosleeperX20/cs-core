
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, diagonals, anti_diagonals, cols):
            return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                result.append(["".join(r) for r in state])
                return

            for col in range(n):
                if not is_safe(row, col, diagonals, anti_diagonals, cols):
                    continue

                # Place queen
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                state[row][col] = 'Q'

                # Move to next row
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # Remove queen (backtrack)
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                state[row][col] = '.'

        result = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return result
