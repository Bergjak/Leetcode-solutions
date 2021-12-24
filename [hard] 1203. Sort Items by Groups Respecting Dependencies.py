from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # Items in the same group are next to eachother in the result
        # beforeItems[i] is a list of items that need to come before i

        # So, I think (1) do a topsort within the groups and then sort the groups according to the topsort
        # (2) do a topsort of the groups and generate the array according to that ordering
        groups = defaultdict(set)
        elements_to_groups = {}
        for i in range(n):

            # This makes it so that elements not assigned to groups are assigned to a size 1 group,
            # which will be useful when topsort is performed between groups
            if group[i] == -1:
                m += 1
                group[i] = m

            groups[group[i]].add(i)
            elements_to_groups[i] = group[i]

        # For the elements not in a group (that is, group[i] == -1), I will just consider each of them to be in their
        # own group and so will ignore them until part (2) of the algorithm

        # So, now I will do topsort on each group. For the topsort, I will get the dependencies within the group.
        sorted_groups = defaultdict(list)
        between_group_dependencies = defaultdict(set)

        def topsort(group_num):
            len_of_group = len(groups[group_num])
            indegree = defaultdict(int)
            graph = defaultdict(set)
            no_in_group_dependencies = True

            for item in groups[group_num]:
                for comes_before in beforeItems[item]:
                    if comes_before in groups[group_num]:
                        indegree[item] += 1
                        graph[comes_before].add(item)
                        no_in_group_dependencies = False
                    else:
                        # This means that whichever group comes_before is in has to come before group group_num
                        between_group_dependencies[elements_to_groups[comes_before]].add(group_num)

            if no_in_group_dependencies:
                sorted_groups[group_num] = list(groups[group_num])
                return True

            q = deque([i for i in groups[group_num] if indegree[i] == 0])
            result = []

            while q:
                node = q.popleft()
                result.append(node)

                for vertex in graph[node]:
                    if indegree[vertex] > 0:
                        indegree[vertex] -= 1
                        if indegree[vertex] == 0:
                            q.append(vertex)

            if len(result) < len_of_group:
                return False
            sorted_groups[group_num] = result
            return True

        for key in groups.keys():
            if not topsort(key):
                # This is if a dependency cycle is found during a topsort
                return []

        sorted_between_groups = []
        indegree = defaultdict(int)
        res = []

        for key, dependencies_btwn_groups in between_group_dependencies.items():
            for node in dependencies_btwn_groups:
                indegree[node] += 1

        if not indegree:
            for key in sorted_groups.keys():
                res.extend(sorted_groups[key])
            return res

        q = deque([i for i in groups.keys() if indegree[i] == 0])

        while q:
            node = q.popleft()
            sorted_between_groups.append(node)

            for vertex in between_group_dependencies[node]:

                if indegree[vertex] > 0:
                    indegree[vertex] -= 1
                    if indegree[vertex] == 0:
                        q.append(vertex)

        for i in sorted_between_groups:
            res.extend(sorted_groups[i])

        return res if len(res) == n else []