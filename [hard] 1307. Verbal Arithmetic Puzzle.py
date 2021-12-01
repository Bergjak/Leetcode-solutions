import itertools

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        '''
        The general idea in this program is to treat each power of 10 of the equation as its own level, as this
        makes the backtracking process much faster than just enumerating all possible maps from letters to numbers.
        So, when I saw a "level of the equation," what I mean is all i for chars[i][level] and result[level].
        Every character on that "level" maps to a number that will be multiplied by 10**level. Then in the backtrack,
        since it is possible that the current levels are not equal because the equality requires input from the next
        higher level, I pass to the next level if and only if Left_hand_side % 10**level == Right_hand_side % 10**level
        
        This solution happens to be 100% faster than the other solutions
        '''

        length = max(len(x) for x in words)

        # If either of these conditions hold, then it is impossible to have equality
        if len(result) - 2 >= length or length > len(result):
            return False

        # I reverse the words so that the first letters are multiplied by the lowest powers of 10 during the backtrack
        result = result[::-1]
        for i in range(len(words)):
            words[i] = words[i][::-1]

        # I am now making a set of the last letters of each word, which are not allowed to be equal to zero.
        # Despite what the problem description says, you are supposed to let single letter words (eg "C") possibly equal zero
        letters = set(result)
        if len(result) > 1:
            no_zeros = set(result[0])
        else:
            no_zeros = set()

        # I am now grabbing all of the letters and continuing to add letters to no_zeros when appropriate
        for x in words:
            letters |= set(x)
            if len(x) > 1:
                no_zeros.add(x[-1])
        letters = list(letters)

        # I am now taking the transpose of the matrix of words, which makes it so that each letter is sitting with every other letter
        # of the same power of ten. For example, letters in levels[2] will all be multiplied by 10**2
        for i in range(len(words)):
            while len(words[i]) < length:
                words[i] += '#'
        levels = list(zip(*words))
        for i in range(len(levels)):
            levels[i] = list(levels[i])
            for x in range(len(levels[i]) - 1, -1, -1):
                if levels[i][x] == '#':
                    levels[i].pop(x)

        # This is to make the base case neater
        while len(levels) < len(result):
            levels.append([])
        length_of_result = len(result)
        num_set = set(i for i in range(10))
        letters_to_nums = {}

        def backTrack(level, lhs, rhs):
            if level == length_of_result:
                return lhs == rhs

            available_chars = list(set(levels[level] + [result[level]]) - set(letters_to_nums.keys()))
            available_nums = list(num_set - set(letters_to_nums.values()))

            if len(available_chars) > len(available_nums):
                return False

            # Try out all correctly sized permutations of available numbers that we can choose at this level of the equation
            for perm in itertools.permutations(available_nums, len(available_chars)):
                fail = False

                for idx, num in enumerate(perm):
                    if num == 0 and available_chars[idx] in no_zeros:
                        fail = True
                        for i in range(idx):
                            del letters_to_nums[available_chars[i]]
                        break

                    letters_to_nums[available_chars[idx]] = num

                if fail:
                    continue

                LHS, RHS = lhs, rhs

                for char in levels[level]:
                    LHS += (10 ** level) * letters_to_nums[char]

                RHS += (10 ** level) * letters_to_nums[result[level]]
                
                # this is equivalent to (LHS % 10 ** level == RHS % 10 ** level) but waaay faster
                if LHS//10**level % 10 == RHS//10**level % 10 and backTrack(level + 1, LHS, RHS):
                    return True

                # This is where I backtrack
                for i in range(len(perm)):
                    del letters_to_nums[available_chars[i]]

            return False

        return backTrack(0, 0, 0)
