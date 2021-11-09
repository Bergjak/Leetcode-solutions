from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_mask_counter = defaultdict(int)
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - 97)
            word_mask_counter[mask] += 1

        res = []
        for puzzle in puzzles:
            needed_bit = 1 << (ord(puzzle[0]) - 97)
            res.append(word_mask_counter[needed_bit])
            puzzle_mask = 0
            for c in puzzle[1:]:
                puzzle_mask |= 1 << (ord(c) - 97)
            og_puzzle_mask = puzzle_mask

            while puzzle_mask:
                res[-1] += word_mask_counter[puzzle_mask | needed_bit]
                puzzle_mask = (puzzle_mask - 1) & og_puzzle_mask

        return res