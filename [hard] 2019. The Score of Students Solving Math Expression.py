from functools import cache

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        upper_bound = 1000

        @cache
        def waysToCompute(expression):
            splits = set()
            for i, c in enumerate(expression):
                if c in '+*':
                    for a in waysToCompute(expression[:i]):
                        if a <= upper_bound:
                            for b in waysToCompute(expression[i + 1:]):
                                if b <= upper_bound:
                                    if c == '*':
                                        splits.add(a * b)
                                    else:
                                        splits.add(a + b)
            return splits or set([int(expression)])

        numz = waysToCompute(s)
        correct_answer = eval(s)
        score = 0

        for x in answers:
            if x == correct_answer:
                score += 5
            elif x in numz:
                score += 2

        return score