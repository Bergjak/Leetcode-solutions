from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # We can solve slowly by counting the indegree to each letter in words that is preceded by other letters in words that are
        # in the prefix of target, and then the indegree count of a node is the sum of the indegree of the nodes going into it
        # What I can do is, for all j in words[j][i] over i = 1,...,n-1 I can get the frequency of each each character

        # So, for each target[i] in words, I want to know how many prefixes target[:i] are present
        n, m = len(words[0]), len(words)
        frequency = [defaultdict(int) for _ in range(n)]
        MOD = 10 ** 9 + 7

        for i in range(n):
            for j in range(m):
                frequency[i][words[j][i]] += 1

        # Level 1 will be 0...n and each level1[i] will be the sum of all target[0] before i * frequency[i][target[1]]
        # then level2 will be 0...n and each level2[i] will be the sum(level1[j] for j < i) * frequency[i][target[2]]
        # But the summation part of prior levels can be sped up by taking prefix sums. So, I do that.

        levels = [[0] * n for _ in range(len(target))]
        levels[0][0] = frequency[0][target[0]]

        for i in range(1, n):
            levels[0][i] = levels[0][i - 1] + frequency[i][target[0]]

        for j in range(1, len(target)):
            for i in range(j, n):
                                # This counts prefixes of target               
                levels[j][i] = (levels[j - 1][i - 1] * frequency[i][target[j]] + levels[j][i - 1]) % MOD
                                                                             # ^^^This is just for prefix sum, to speed up the algorithm
                    
        return levels[-1][-1] % MOD
