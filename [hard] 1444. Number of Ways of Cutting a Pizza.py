from functools import cache
from collections import defaultdict

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        row_apples = defaultdict(list)
        col_apples = defaultdict(list)
        MOD = 10 ** 9 + 7

        # We are labeling where apples are located, which will allow for quicker lookup of apple positions
        for idx, row in enumerate(pizza):
            for c_idx, x in enumerate(row):
                if x == "A":
                    row_apples[idx].append(c_idx)
                    col_apples[c_idx].append(idx)

        @cache
        def cut(r, c, kut):
            if kut == k - 1:
                # We have made k pieces, and so we get to count this sequence of cuts
                return 1

            ans = 0

            # This loop and the next is to ensure that there are apples on each side of the cut, which is the condition we need to ensure
            # in order to make a legitimate cut.
            for new_horizontal_cut_idx in range(r + 1, m):
                apples_on_top = apples_on_bot = False

                for prev_row in range(r, new_horizontal_cut_idx):
                    if row_apples[prev_row] and row_apples[prev_row][-1] >= c:
                        apples_on_top = True
                        break
                if apples_on_top:
                    for prev_row in range(new_horizontal_cut_idx, m):
                        if row_apples[prev_row] and row_apples[prev_row][-1] >= c:
                            apples_on_bot = True
                            break

                if apples_on_top and apples_on_bot:
                    ans += cut(new_horizontal_cut_idx, c, kut + 1) % MOD

            for new_vertical_cut_idx in range(c + 1, n):
                apples_on_left = apples_on_right = False

                for prev_col in range(c, new_vertical_cut_idx):
                    if col_apples[prev_col] and col_apples[prev_col][-1] >= r:
                        apples_on_left = True
                        break
                if apples_on_left:
                    for prev_col in range(new_vertical_cut_idx, n):
                        if col_apples[prev_col] and col_apples[prev_col][-1] >= r:
                            apples_on_right = True
                            break

                if apples_on_left and apples_on_right:
                    ans += cut(r, new_vertical_cut_idx, kut + 1) % MOD

            return ans

        return cut(0, 0, 0) % MOD