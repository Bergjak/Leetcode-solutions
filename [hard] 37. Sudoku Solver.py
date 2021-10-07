class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # So, for each empty cell, you can determine its set of possible moves
        # Then, you can try a possible move. If the move does not work out, then undo it
        # and try a different move

        stack = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == '.']
        # So, you descend the stack and then backtrack by ascending the stack and unpainting the cell

        # this will be a function that checks the ~27 cells that coloring the cell (r, c) depends on.
        # You will get the possible numbers by taking the difference with options.
        options = set([str(i) for i in range(1, 10)])

        def choices(r, c):
            R, C = 3 * (r // 3), 3 * (c // 3)
            block_row_col = set()
            for i in range(R, R + 3):
                for j in range(C, C + 3):
                    block_row_col.add(board[i][j])
            for i in range(9):
                block_row_col.add(board[r][i])
                block_row_col.add(board[i][c])
            return options - block_row_col

        def back(stack_idx):
            if stack_idx == -1: return True
            r, c = stack[stack_idx]
            ops = list(choices(r, c))

            for x in ops:
                board[r][c] = x
                if back(stack_idx - 1): return True
                board[r][c] = '.'

        back(len(stack) - 1)