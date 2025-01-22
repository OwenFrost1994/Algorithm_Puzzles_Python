from typing import List
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        x = max(cnt.values())
        s = sum(v == x for v in cnt.values())
        return max(len(tasks), (x - 1) * (n + 1) + s)
        # ct = Counter(tasks)
        # tasks = []
        # sche = []
        # for key in ct.keys():
        #     heapq.heappush(tasks, [ct[key], key])
        # while len(tasks) > 0:
        #     l = len(tasks)
        #     for i in range(l):
        #         task = tasks.pop()
        #         sche.append(task[1])
        #         task[0] -= 1
        #         if task[0] != 0:
        #             tasks.insert(0, task)
        #     if l <= n:
        #         sche = sche + ["idle"] * (n - l + 1)
        # while sche[-1] == "idle":
        #     sche.pop()
        # return len(sche)

solution = Solution()
print(solution.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1))
print(solution.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(solution.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
print(solution.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))