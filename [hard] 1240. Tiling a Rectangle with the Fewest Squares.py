class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n == m:
            return 1
        max_square_size = min(m, n)
        # The backtracking could perhaps also be done by first trying for size 2, then size 3, then size 4, etc. and then returning whichever
        # size gives the first True

        board = [[0] * n for _ in range(m)]

        # I will draw by filling in with 1s

        def build(built_squares, limit_of_squares):
            if built_squares > limit_of_squares:
                return False

            x, y = None, None

            for i in range(n):
                for j in range(m):
                    if board[j][i] == 0:
                        x, y = j, i
                        break
                if x != None and y != None:
                    break

            if (x, y) == (None, None):
                # No uncolored cell was found, so you're done
                return True

            for dsquare in range(max_square_size):
                # Now, I build the square, call function again, unbuild the square, repeat

                if x + dsquare >= m or y + dsquare >= n or board[x + dsquare][y] or board[x][y + dsquare] or \
                        board[x + dsquare][y + dsquare]:
                    return False

                for i in range(x, x + dsquare + 1):
                    for j in range(y, y + dsquare + 1):
                        board[i][j] = 1

                if build(built_squares + 1, limit_of_squares):
                    return True

                for i in range(x, x + dsquare + 1):
                    for j in range(y, y + dsquare + 1):
                        board[i][j] = 0

            return False

        for size in range(2, 14):
            if build(0, size):
                return size

        return -1  # "either impossible or more than 13 squares are needed"