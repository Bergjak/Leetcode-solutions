import heapq
from collections import defaultdict

class AutocompleteSystem:

    def insert(self, word, f):
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {"#": defaultdict(int), 'heap': []}
            cur = cur[w]
            if word not in cur['#']:
                cur["#"][word] = f - 1
            cur['#'][word] += 1
            heapq.heappush(cur['heap'], (-cur['#'][word], word))

    def search(self, word, cur):
        if word not in cur:
            return ([], {})
        cur = cur[word]
        words = []
        while cur['heap'] and len(words) < 3:

            # This is for lazy deletions
            while cur['heap'] and -cur['heap'][0][0] != cur['#'][cur['heap'][0][1]]:
                heapq.heappop(cur['heap'])

            if cur['heap']:
                words.append(heapq.heappop(cur['heap'])[1])

        for w in words:
            heapq.heappush(cur['heap'], (-cur['#'][w], w))

        return (words, cur)

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.cur_level = {}
        for idx, sentence in enumerate(sentences):
            self.insert(sentence, times[idx])
        self.new_word = []

    def input(self, c: str) -> List[str]:
        # So, when I get a hashstag, I need to put the typed sentence (the sequence of input from the start of the program or from the
        # start after the most recent hashtag) into the sentence counter and increment the sentences frequency.
        # I think in every node of the trie, have a '#' entry that contains a defaultdict with a counter of the words whose prefixes
        # are contained in that path of the trie and a heap that contains tuples (-freq, word) and then do lazy deletions to
        # remove the words whose counter frequency does not match the reported frequency in the heap
        if c == '#':
            self.insert(''.join(self.new_word), 1)
            self.new_word.clear()
            return

        # first function call of the input sentence:
        if not self.new_word:
            res = self.search(c, self.trie)
        else:
            res = self.search(c, self.cur_level)

        self.new_word.append(c)
        self.cur_level = res[1]
        return res[0]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)