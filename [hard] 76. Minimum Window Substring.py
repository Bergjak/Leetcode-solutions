import sys
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        got = {k: False for k in needed.keys()}
        quantity_needed = len(got)
        left = 0
        LEFT = RIGHT = 0
        best = sys.maxsize

        for r in range(len(s)):
                
            # We now need one less of character s[r], and so we decrement the count of how many s[r] we need.
            needed[s[r]] -= 1
            if needed[s[r]] == 0:
                # Once quantity_needed equals zero, that means we have captured every character (including duplicates) in our sliding window
                # and we are therefore ready to start taking answer candidates.
                quantity_needed -= 1

            # If needed[s[r]] <= 0, then between the left and right pointer, we have captured enough chars s[r] that we can afford to dump s[r] out
            # the leftside of our window. However, if we hit another char with our left pointer that is also needed, and we have no extras of that char
            # (i.e., if needed[s[left]] >= 0), then we must stop sliding the left pointer rightward, as we need that character to capture the whole substring.
            if needed[s[r]] <= 0:
                while left < r and needed[s[left]] < 0: 
                    
                    # As the left pointer slides rightward, we need to keep track of what new characters we will need as a result of kicking chars out of the window.
                    needed[s[left]] += 1

                    left += 1

            # This is the case if we have an answer, and so we initialize best to sys.maxsize so that we can always get a first choice once quantity_needed <= 0
            if quantity_needed <= 0 and r - left + 1 < best:
                best = r - left + 1
                LEFT = left
                RIGHT = r + 1
        
        # Rather than save the candidate string to be returned, which is O(n), we just save the LEFT and RIGHT pointers of the window which captures the substring, which is O(1)
        return s[LEFT: RIGHT]
