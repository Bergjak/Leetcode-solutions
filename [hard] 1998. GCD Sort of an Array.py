from collections import defaultdict

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        # I think you can sort nums if there is a connected component spanning the whole graph given by elements of nums x, y and edges gcd(x, y) connecting x <--> y.
        # You can also sort nums if the collection of sorted connected components is a sorted graph. But that sorting will have
        # to respect the ordering of subsequences in nums. Eg, if we had [a,g,b,f,e,c,d] and {a,d,g}, {b,c,e,f} are connected,
        # then we can sort by making [a,_,_,d,_,_,g] but we'd fail if {a,f,g}, {b,c,d,e} since [a,f,_,g,_,_,_] is not sorted
        #                            [_,b,c,_,e,f,_]                                           [_,_,b,_,c,d,e]

        check = sorted(nums)
        if check == nums:
            return True

        factors = defaultdict(set)
        n = len(nums)

        def factor(x, idx):
            factors[x].add(idx)
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    factors[i].add(idx)
                    factors[x // i].add(idx)

        for idx, x in enumerate(nums):
            factor(x, idx)

        p = [i for i in range(n)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            Ux, Uy = find(x), find(y)
            p[Ux] = Uy

        for edges in factors.values():
            root = edges.pop()
            for x in edges:
                union(root, x)
        p = list(map(find, p))

        unions = defaultdict(list)
        for idx, x in enumerate(p):
            unions[x].append(idx)
        # Now, I have to grab each group in each union. Then I need to grab the elements in nums which are at those indices. Then I need to sort those elements. Then I need to
        # over write the indices of nums with this sorted list

        for union in unions.values():
            sorted_list = []
            for idx in union:
                sorted_list.append(nums[idx])
            sorted_list.sort(reverse=True)
            for idx in union:
                nums[idx] = sorted_list.pop()

        return nums == check