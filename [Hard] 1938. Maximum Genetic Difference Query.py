from collections import defaultdict

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        def insert(trie, val):
            cur = trie
            bitmask = bin(val)[2:].zfill(20)
            first_new_branch_idx = None
            for idx, bit in enumerate(bitmask):
                if bit not in cur:
                    cur[bit] = {}
                    if first_new_branch_idx is None:
                        first_new_branch_idx = idx
                cur = cur[bit]
            return first_new_branch_idx

        def remove(trie, val, remove_idx):
            cur = trie
            bitmask = bin(val)[2:].zfill(20)
            for idx, bit in enumerate(bitmask):
                if idx == remove_idx:
                    del cur[bit]
                    break
                cur = cur[bit]

        def maxXor(trie, val):
            cur = trie
            bitmask = bin(val)[2:].zfill(20)
            result = ''

            for bit in bitmask:
                if bit == '1':
                    if '0' in cur:
                        cur = cur['0']
                        result += '1'  # 1 ^ 0 == 1
                    else:
                        cur = cur['1']
                        result += '0'  # 1 ^ 1 == 0
                else:
                    if '1' in cur:
                        cur = cur['1']
                        result += '1'  # 0 ^ 1 == 1
                    else:
                        cur = cur['0']
                        result += '0'  # 0 ^ 0 == 0
            return int(result, 2)

        newQueries = defaultdict(list)  # genetic val: [(val, idx_in_quries)]
        res = [0] * len(queries)
        for idx, (node, val) in enumerate(queries):
            newQueries[node].append((val, idx))
            # So, in the DFS, each time I arrive at a node, I need to ask what queries are at this node

        graph = defaultdict(list)
        start_idx = None
        for child, parent in enumerate(parents):
            if parent == -1:
                start_idx = child
            graph[parent].append(child)

        def dfs(node, ogTrie):
            for val, idx in newQueries[node]:
                res[idx] = maxXor(ogTrie, val)

            for child in graph[node]:
                remove_idx = insert(ogTrie, child)
                dfs(child, ogTrie)
                # The remove operation would just have to delete from the trie the first new branch that
                # is added, if any at all
                if remove_idx is not None:
                    remove(ogTrie, child, remove_idx)

        TRIE = {}
        insert(TRIE, start_idx)
        dfs(start_idx, TRIE)

        return res