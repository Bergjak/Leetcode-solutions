from collections import defaultdict, Counter

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # I think the order in which columns and rows are swapped does not matter. Therefore, we can count how many row swaps need to occur and then we can count how many column
        # swaps need to occur. But since we can transpose the matrix after fixing the rows, we can just fix the rows again. Hence, we just need to figure out how to count
        # how many row swaps need to occur to make rows good. Thus, we can turn each row into a base 10 number. If there is not exactly 2 numbers in the resulting array of rows
        # converted to numbers, then making a chess board is impossible. If there is exactly 2, then we need to make them alternating in the cheapest fashion possible, and
        # so we count how many of each are at the even indices. The number that appears most at even indices is the one we will keep at the even indices. Then I simply
        # count how many times a number is at the wrong index; that number is res. Then I convert the base 10 numbers into binary, place the bits into a matrix, and then
        # transpose the matrix and do the whole thing again; but since the matrix is transposed, we are now operating on the columns. I then return half of the bad indices
        # that I counted, since it takes 2 indices to do a single swap.

        # This is to make sure that we have the correct amount of zeros and ones.
        ones = 0
        zeros = 0
        for row in board:
            for x in row:
                if x:
                    ones += 1
                else:
                    zeros += 1
        if ones < zeros: ones, zeros = zeros, ones
        if not (ones == zeros or ones - 1 == zeros):
            return -1

        n = len(board)
        res = 0
        row_nums = []
        for row in board:
            num = 0

            for idx, bit in enumerate(row):
                num |= bit << idx

            row_nums.append(num)
        count_nums = Counter(row_nums)
        if len(count_nums.keys()) != 2:
            return -1

        if n % 2 == 0:
            if len(set(count_nums.values())) != 1:
                return -1
            vote = defaultdict(int)
            for i in range(0, n, 2):
                vote[row_nums[i]] += 1
            even_index = max(vote.items(), key=lambda x: x[1])[0]

            for k in count_nums:
                if k != even_index:
                    odd_index = k
            # just count how many are placed in the wrong index
            for i, num in enumerate(row_nums):
                if i % 2 and num != odd_index:
                    res += 1
                elif i % 2 == 0 and num != even_index:
                    res += 1
            fixed_row = [even_index, odd_index] * (n // 2)
        else:
            odd_check = sorted(count_nums.items(), key=lambda x: x[1])
            if odd_check[0][1] + 1 != odd_check[1][1]:
                return -1
            even_index = odd_check[1][0]
            odd_index = odd_check[0][0]
            for i, num in enumerate(row_nums):
                if i % 2 and num != odd_index:
                    res += 1
                elif i % 2 == 0 and num != even_index:
                    res += 1
            fixed_row = [even_index] + [odd_index, even_index] * (n // 2)

        new_board = []
        for x in fixed_row:
            row = bin(x)[2:].zfill(n)
            new_board.append([])
            for i in row:
                new_board[-1].append(int(i))

        if res % 2:
            return -1

        row_nums = []
        for col in zip(*new_board):
            num = 0

            for idx, bit in enumerate(col):
                num |= bit << idx

            row_nums.append(num)

        count_nums = Counter(row_nums)
        if len(count_nums.keys()) != 2:
            return -1

        if n % 2 == 0:
            if len(set(count_nums.values())) != 1:
                return -1
            vote = defaultdict(int)
            for i in range(0, n, 2):
                vote[row_nums[i]] += 1
            even_index = max(vote.items(), key=lambda x: x[1])[0]
            for k in count_nums:
                if k != even_index:
                    odd_index = k
            # just count how many are placed in the wrong index
            for i, num in enumerate(row_nums):
                if i % 2 and num != odd_index:
                    res += 1
                elif i % 2 == 0 and num != even_index:
                    res += 1
        else:
            odd_check = sorted(count_nums.items(), key=lambda x: x[1])
            if odd_check[0][1] + 1 != odd_check[1][1]:
                return -1
            even_index = odd_check[1][0]
            odd_index = odd_check[0][0]
            for i, num in enumerate(row_nums):
                if i % 2 and num != odd_index:
                    res += 1
                elif i % 2 == 0 and num != even_index:
                    res += 1

        if res % 2:
            return -1
        return res // 2