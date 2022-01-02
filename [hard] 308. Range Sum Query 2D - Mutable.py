class SegmentTree:

    def __init__(self, values):
        length = 1
        while length < len(values):
            length *= 2
        while len(values) < length:
            values.append(0)
        self.n = len(values)
        self.tree = [0] * self.n + values
        for k in range(2 * self.n - 1, 1, -1):
            self.tree[k // 2] += self.tree[k]


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        vals = []
        for row in matrix:
            vals.extend(row)
        segTree = SegmentTree(vals)
        self.tree = segTree.tree
        self.tree_length = segTree.n

    def update(self, row: int, col: int, val: int) -> None:
        # I can just collapse the matrix to 1D and then establish a mapping for the sumRegion function
        # So, I'd just need to write a segment tree with summation and updates
        idx = (row * self.n + col) + self.tree_length
        delta = val - self.tree[idx]
        self.tree[idx] += delta
        parent = idx // 2
        while parent > 0:
            self.tree[parent] += delta
            parent //= 2

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for x in range(row1, row2 + 1):
            left = (x * self.n + col1) + self.tree_length
            right = left + col2 - col1

            while left <= right:
                if left % 2:
                    s += self.tree[left]
                    left += 1
                if right % 2 == 0:
                    s += self.tree[right]
                    right -= 1
                left //= 2
                right //= 2
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)