# 这题挺诡异，你得加上24:00以保证23:59和00:00/00: 13这种最小时间形成闭环，
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        times.append(times[0] + 24 * 60)
        mind = 24*60
        for i in range(1, len(times)):
            mind = min(mind, times[i] - times[i - 1])
        return mind

solution = Solution()
print(solution.findMinDifference(timePoints = ["23:59","00:00"]))
print(solution.findMinDifference(timePoints = ["00:00","23:59","00:00"]))