from collections import defaultdict
from heapq import heappop, heappush


class DinnerPlates:
    """
    So, we have to use the left_keys heap to identify the left_most key whose stack is not full
    and the right_keys heap to identify the right_most key whose stack is not empty.
    So, we should not manage sets of keys (since that's a complicated optimization) but rather just heappop while stacks[left_keys[0]] >= capacity
    and heappop while stacks[right_keys[0]] < 1.
    Finally, when we popAtStack, just put that key in the left_keys heap
    """

    def __init__(self, capacity: int):
        self.stacks = defaultdict(list)
        self.highest_key = 0
        self.left_keys = [0]
        # Contains keys to stacks, tracking leftmost keys with size less than capacity. So, we heappop if the
        # smallest key has its stack reach full capacity

        self.right_keys = []
        # Has -key vals, inserted into here once popped off from left_keys and a keys is put in here whenever
        # a stack has some stuff put in it

        self.cap = capacity

    def push(self, val: int) -> None:
        while self.left_keys and len(self.stacks[self.left_keys[0]]) >= self.cap:
            heappop(self.left_keys)

        if not self.left_keys:
            self.highest_key += 1
            self.left_keys.append(self.highest_key)

        self.stacks[self.left_keys[0]].append(val)

        heappush(self.right_keys, -self.left_keys[0])
        # Since the right heap wants to to track non-empty stacks, we just put all keys from this function into the right heap

    def pop(self) -> int:
        while self.right_keys and len(self.stacks[-self.right_keys[0]]) < 1:
            heappop(self.right_keys)

        if not self.right_keys:
            return -1

        heappush(self.left_keys, -self.right_keys[0])
        # Negative because keys put into self.right_keys are negative for sorting by maximum. Since the left heap wants to track all
        # stacks that are at less than full capacity, we put any stack from this function into the left heap (because we just popped)

        return self.stacks[-self.right_keys[0]].pop()

    def popAtStack(self, index: int) -> int:
        if len(self.stacks[index]) < 1: return -1

        heappush(self.left_keys, index)
        return self.stacks[index].pop()
