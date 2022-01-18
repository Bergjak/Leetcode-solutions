from bisect import bisect_left


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], p: int, s: int) -> int:
        n, m = len(tasks), len(workers)
        workers.sort()
        tasks.sort()

        def possible(size):
            # So, I take the smallest size tasks and then reverse that prefix array
            to_do_list = tasks[:size][::-1]
            P = p
            employees = workers[-size:]

            # Now, iterate through the to do list, checking the largest tasks first
            for task in to_do_list:

                # Find the location of the smallest employee that can solve the task
                idx = bisect_left(employees, task)

                # If there exists an employee that is good enough, remove the smallest such employee
                if idx < len(employees) and employees[idx] >= task:
                    employees.pop(idx)

                # If such an employee does NOT exist, then give the task the pill, and look for a worker
                # that can now solve the task. If such a worker exists, assign the smallest one the task and the pill.
                # Remove that worker from the employee list and subtract P, the number of pills available
                elif idx == len(employees) and P > 0:
                    new_idx = bisect_left(employees, task - s)
                    P -= 1
                    if new_idx < len(employees) and employees[new_idx] >= task - s:
                        employees.pop(new_idx)
                    else:
                        return False

                else:
                    return False

            # If we were able to accomplish all the tasks, we can return True
            return True

        # We can perform binary search on the number of doable tasks because, if we can do x tasks,
        # then we can do x - i tasks for i < x. So, we just find the largest possible x and return it.
        l, r = 0, min(n, m)
        while l < r:
            mid = (l + r + 1) // 2

            if possible(mid):
                l = mid
            else:
                r = mid - 1

        return l
