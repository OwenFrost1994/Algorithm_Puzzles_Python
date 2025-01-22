from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time = [0]*n
        curr = -1
        tasks = []
        for log in logs:
            task = log.split(":")
            id = int(task[0])
            t = int(task[2])
            if task[1] == "start":
                if tasks:
                    time[tasks[-1]] += t - curr
                tasks.append(id)
                curr = t
            else:
                id = tasks.pop()
                time[id] += t - curr + 1
                curr = t + 1
        return time

solution = Solution()
print(solution.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(solution.exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
print(solution.exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))