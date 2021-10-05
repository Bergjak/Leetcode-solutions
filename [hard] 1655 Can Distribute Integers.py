from collections import Counter
class Solution:
    def canDistribute(nums, Q) -> bool:
        same_items = sorted(Counter(nums).values())
        m, n = len(Q), len(same_items)
        masks = [sum(Q[i] for i in range(m) if mask & 1<<i) for mask in range(1<<m)]  # I call entries of this array "Q_sums"
        valids = set()   # These are the bitmasks that correspond to possible maps same_items[idx] --> Q[i] for all i in mask
        winner = (1<<m) - 1
        for idx in range(n):
            new_valids = set()
            for mask, x in enumerate(masks):
                if same_items[idx] >= x:
                    if mask == winner: return True
                    new_valids.add(mask)
            for x in valids.copy():
                for y in new_valids:
                    if x & y == 0:
                        merged_mask = x | y
                        if merged_mask == winner: return True
                        valids.add(merged_mask)
            valids.update(new_valids)
        return False