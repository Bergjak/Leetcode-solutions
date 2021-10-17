from collections import defaultdict, deque
class Solution:

    def insert(self, word, idx):
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {}
                cur[w]['count'] = 0
            cur = cur[w]
            cur['count'] += 1
            cur['idx'] = idx

    def wordsAbbreviation(self, words):
        # So, we only abbreviate by replacing the longest suffix (modulo the final character) such that the abbreviation is unique
        # So, it seems like we can use the divergence point between words in a trie for determining the abbreviation
        # And we could group words by their length since only words of equal length have any chance of colliding
        # In fact, only words of equal length and same first and last character can collide.
        similars = defaultdict(list)  # This will be lists of words all having the same length and equal first and last characters
        res = [None] * len(words)     # Abbreviations of words are required to be returned at the same indices as they are given in the input
        for idx, word in enumerate(words):
            length, first, last = len(word), word[0], word[-1]
            if length <= 3:
                res[idx] = word
                continue
            similars[(length, first, last)].append((word, idx))

        # So, what we do now is put words of a similar category in a trie. Then after all the words are in, we do bfs on the trie. As we insert
        # words, at each level of the trie, I should have a counter of how many words are at that level. Then, if on a branch of the trie,
        # the counter becomes 1, then I append to res prefix_so_far + str(length - len(prefix_so_far)) + last where prefix_so_far does not include
        # the first letter at which 'count' == 1
        for (length, first, last), similar_words in similars.items():
            self.trie = {}
            if len(similar_words) == 1:
                idx = similar_words[0][1]
                res[idx] = first + str(length - 2) + last
                continue
            for word, idx in similar_words:
                self.insert(word, idx)
            q = deque([('', self.trie)])  # prefix_so_far
            while q:
                prefix, cur = q.popleft()
                for k in cur.keys():
                    if k == 'count' or k == 'idx': continue
                    if 'count' in cur and cur['count'] == 1:
                        idx = cur['idx']
                        if length - len(prefix) > 2:
                            res[idx] = prefix + str(length - len(prefix) - 1) + last
                        else:
                            res[idx] = words[idx]
                        continue
                    q.append((prefix + k, cur[k]))
        return res