from collections import defaultdict
class Solution:
    def findWords(self, grid: List[List[str]], words: List[str]) -> List[str]:
        # Make a trie of the words. At each step of bfs ([r, c, visited_trajectory]), check if any word in trie begins with letters words[r][c] and check
        # if words[r][c] is the continuation of any word; if words[r][c] is the final letter in a word, then add it to res
        # Abandon a trajectory if it cannot be the continuation of a word
        # So, if upon performing a search for a word, and the result of search(word) is False, then the prefix you are hunting
        # cannot be found. Thus, don't put it on the stack.
        # Further, we only can enter a cell from four different directions. So, keep a global visited that counts how many times you have entered a cell. You will never need
        # to enter the same cell more than 4 times, so disallow entering the cell more than 4 times.
        res = set()
        self.trie = {}
        # Setting up trie

        def insert(word):
            cur = self.trie
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur['#'] = '#'  # If # in self.trie[some_letter], then that's the end of a word

        def search(word):
            cur = self.trie
            for w in word:
                if w not in cur:
                    return False
                cur = cur[w]
            if '#' in cur:
                res.add(word)
            return True

        for word in words:
            insert(word)

        # Doing bfs
        m, n, stack, visit_counter = len(grid), len(grid[0]), [], defaultdict(int)
        for i in range(m):
            for j in range(n):
                stack.append((i, j, grid[i][j], {(i, j)}))
                search(grid[i][j])
        while stack:
            r, c, word, visited = stack.pop()
            for u, v in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= u < m and 0 <= v < n and (u, v) not in visited and search(word + grid[u][v]) and visit_counter[(u, v)] < 4:
                    visit_counter[(u, v)] += 1
                    stack.append((u, v, word + grid[u][v], visited | {(u, v)}))
        return res
