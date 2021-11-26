import math

class Solution:
    def kthSmallestPath(self, D: List[int], k: int) -> str:
        # So, we have math.comb(H+V, H) choices since we are modeling pascal's triangle,
        # and we want to return the k'th choice (in lexicographical order). So, say we have k > math.comb(H+V-1, H-1).
        # Then it must be the case that result starts with V, since the number of remaining options
        # starting with H is less than k, and so if we chose H then we'd never be able to reach the k'th choice.
        # After the first choice, k -= math.comb(H+V-1, H-1) and then we subtract 1 from V and then recompute total.
        # We did k -= math.comb(H+V-1, H-1) because we are now restricted to the search space of options NOT beginning with H,
        # so we remove from the search space all options that begin with H. And then this process continues until we run out
        # of options, since every suffix follows the same logic as the full string.

        H, V = D[1], D[0]
        res = []

        while H and V:
            num_of_suffixes_starting_with_H = math.comb(H - 1 + V, H - 1)

            if k > num_of_suffixes_starting_with_H:
                res.append('V')
                k -= num_of_suffixes_starting_with_H
                V -= 1
            else:
                res.append('H')
                H -= 1

        return ''.join(res + ['H'] * H + ['V'] * V)