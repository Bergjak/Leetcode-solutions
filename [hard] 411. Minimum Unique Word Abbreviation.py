class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        candidates = set()
        t = len(target)

        for word in dictionary:
            if len(word) == t: candidates.add(word)
        if not candidates: return str(t)

        '''
	If a word in the dictionary does not have the same length as target, then there is no possible way that any of their
	abbreviations could collide. So, we just filter out everything that does not have the correct length.

	Further, it is only possible for a word in the dictionary to collide with target if target[i] == word[i] for some i. So, we 
	will make bitmasks of all differences of words in dictionary against target, such that if target[i] == word[i], 
	we leave 1<<i as a zero in the bitmask; we put those bitmasks in a set called diffs. Then for all bitmasks m of target, we will
	let zeros correspond to abbreviations (e.g., if target == 'kittycat', then abbreviate('00000111') == "5cat").
	Then a bitmask m is valid if and only all(m & d != 0 for d in diffs). For example, if we have target == 'kitcat' and 'bigcat' in
	the dictionary, then we will have the difference mask d == 111000 and so any valid abbreviation of target must
	not delete all the letters 'kit', and therefore a valid mask would be of the form 011111 as then 011111 & 111000 == 011000 > 0
	and then we'd return abbreviate(011111) == k5.
	'''

        diffs = set()
        for word in candidates:
            diff_num = 0
            for i, (c1, c2) in enumerate(zip(target, word)):
                if c1 != c2: diff_num |= 1 << i
            diffs.add(diff_num)

        def abbreviate(mask):
            i = 0
            res = ''
            while i < t:

                if not mask & (1 << i):
                    num = 0
                    while i < t and not mask & (1 << i):
                        num += 1
                        i += 1
                    res += str(num)

                if i >= t: break

                res += target[i]

                i += 1
            return res

        best = target
        for mask in range(1 << t):
            if all(mask & d for d in diffs):
                word = abbreviate(mask)
                if len(word) < len(best):
                    best = word
        return best
