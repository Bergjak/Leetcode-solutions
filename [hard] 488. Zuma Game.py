from functools import cache
from collections import deque

class Solution:
    def findMinStep(self, board: str, Hand: str) -> int:

        visited = set()
        board, Hand = list(board), list(Hand)
        q = deque([(0, board, Hand)])

        @cache
        def removal(string):
            string = list(string)
            rem = False
            i = 0

            while i + 2 < len(string):

                if i + 2 < len(string) and string[i] == string[i + 1] == string[i + 2]:
                    j = i + 2
                    while j < len(string) and string[j] == string[i]:
                        j += 1
                    string = string[:i] + string[j:]
                    rem = True  # this is in case we have something like xbbbxx and then we remove bbb and get xxx and then we need to call function again

                i += 1
            if rem:
                return removal(tuple(string))
            return string

        while q:

            score, b, hand = q.popleft()
            if score > 2 and len(set(hand)) + 2 < len(set(b)): continue
            local_vis = set()

            for idx, x in enumerate(hand):
                if x in local_vis: continue
                local_vis.add(x)
                new_hand = hand[:idx] + hand[idx + 1:]
                vis_hand = tuple(new_hand)

                for i in range(len(b) + 1):

                    new_b = b[:]
                    new_b.insert(i, x)
                    new_b = removal(tuple(new_b))
                    vis_b = tuple(new_b)

                    if (vis_b, vis_hand) not in visited:
                        if not new_b:
                            return score + 1
                        visited.add((vis_b, vis_hand))
                        q.append((score + 1, new_b, new_hand))
        return -1