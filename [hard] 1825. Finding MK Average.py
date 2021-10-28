from sortedcontainers import SortedList
from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        self.stream = deque()
        self.prefix = [0]
        self.smallest_k = SortedList()
        self.small_k_val = 0
        self.biggest_k = SortedList()
        self.big_k_val = 0
        self.cap = m
        self.k = k

    def addElement(self, num: int) -> None:
        # Notice that changes to small_k (i.e., the sum of the smallest k elements) happen when either (1) the size of the stream
        # exceeds m and so we have to boot out the m'th item, and if that item is part of small_k, then small_k -= m'th_item
        # and small_k += new_smaller or (2) an element is added to the stream that is smaller than some element that's part of the
        # smallest k values
        # So, maybe I can keep a Counter smallest_k that tracks which (and how many) elements are part of the smallest k, and then when
        # an element is added to the stream, I also add that element to a heap, and then I do a heappop, and if the popped element
        # is in the counter, that means I have to change small_k and then find what will replace the item that just got booted

        # So, to track the smallest k elements, I would need to keep a list sorted and be able to quickly identify
        # if one of the elements in that list needs to be removed because the master list/stream exceeded size m. A counter solves
        # that problem. But then, how do I identify what needs to be replaced in small_k? If I kept a sortedlist, then I could remove
        # that element from the sortedlist and then check what sortedlist[k-1] is after that removal, which will always be what needs
        # to be added to small_k, and that takes log(n) time

        self.stream.append(num)
        self.prefix.append(self.prefix[-1] + num)
        k = self.k
        self.smallest_k.add(num)
        self.biggest_k.add(-num)

        if len(self.stream) > self.cap:
            # case 2
            small_idx = self.smallest_k.index(num)
            if small_idx < k:
                # Remove smallest_k[k] instead of k-1 bcuz we already inserted num, and so what used to be smallest_k[k-1] has slid up one spot
                self.small_k_val -= self.smallest_k[k]
                self.small_k_val += num
            big_idx = self.biggest_k.index(-num)
            if big_idx < k:
                self.big_k_val += self.biggest_k[k]
                self.big_k_val += num

            # case 1
            rem = self.stream.popleft()
            # If rem is less than or equal to the largest value of the smallest_k values, then we have to boot rem out of small_k_val
            # since it was in small_k_val, and regardless we need to remove it from self.smallest_k
            if rem in self.smallest_k:
                rem_idx = self.smallest_k.index(rem)
                self.smallest_k.remove(rem)
                # We remove rem in case rem is smallest[k-1], and so this maintains the invariant that
                # smallest_k[k-1] is the largest smallest value that is in the stream
                if rem_idx < k and not rem_idx == small_idx + 1 == k:
                    self.small_k_val -= rem
                    self.small_k_val += self.smallest_k[k - 1]

            if -rem in self.biggest_k:
                rem_idx = self.biggest_k.index(-rem)
                self.biggest_k.remove(-rem)
                if rem_idx < k and not rem_idx == big_idx + 1 == k:
                    self.big_k_val -= rem
                    self.big_k_val -= self.biggest_k[k - 1]

        elif len(self.stream) == self.cap:
            # This happens only once and it is the time that we initialize our k values
            self.small_k_val = sum(self.smallest_k[:k])
            self.big_k_val = -sum(self.biggest_k[:k])

    def calculateMKAverage(self) -> int:

        if len(self.stream) < self.cap: return -1
        # Take the last m elements, remove the largest and smallest k elements, and then compute the average of what remains
        # So, if we did not have to remove anything, then all we would need to do is keep the stream as a prefix sum array
        # and then return (p[-1] - p[-m-1])//m .  Notice that m and k are fixed, and therefore we could keep multiple prefix arrays.
        # If it is somehow possible to keep the value of the sum of the largest k and smallest k elements of the last m,
        # then I can compute (p[-1] - p[-m-1] - small_k - large_k) // (m - 2*k)
        full_sum = self.prefix[-1] - self.prefix[-self.cap - 1]
        return (full_sum - self.small_k_val - self.big_k_val) // (self.cap - 2 * self.k)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()