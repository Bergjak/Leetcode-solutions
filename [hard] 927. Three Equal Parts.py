from bisect import bisect_right

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # The idea here is to generate all prefixes and all suffixes, and then for each prefix[i],
        # I bisect suffixes to see if there exists suffix[idx] == prefix[i], and if this is the case,
        # then I check to see if the subarray in between arr[i: n - idx - 1] also equals prefix[i].
        # So, this is possible because Python does not have an upperbound on the size of integers.
        # Thus, this is a general means of solving these types of problems ("cut array into 3 pieces")
        # and it has O(n * log(n)) time because we are doing n bisections on the suffix array in the worst case.

        n = len(arr)
        pre, suf = [0], [0]

        for i in range(n):
            pre_bit, suf_bit = int(arr[i]), int(arr[~i])
            pre.append(pre[-1] << 1 | pre_bit)
            suf.append(suf_bit << i | suf[-1])

        if pre[-1] == 0:
            return [0, n - 1]

        # If there are M continuous zeros at the end of the array arr, then we need to shift the middle part
        # over to the right by M positions.
        zeros = 0
        while zeros < len(suf) and suf[zeros] == 0: zeros += 1

        for i in range(n):
            idx = bisect_right(suf, pre[i]) - 1

            if n + zeros < idx + i + 1:
                return [-1, -1]

            middle_part = pre[n - idx - 1 + zeros] ^ (pre[i] << (n - idx - 1 + zeros - i))
            if suf[idx] == pre[i] == middle_part:
                return [i - 1, n - idx - 1 + zeros]

        return [-1, -1]