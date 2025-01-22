# 一开始理解错了，第一次攻击在1，持续1，2，第二次攻击在2，那就持续2，3，最后只有三秒
# 如果是攻击在1和4那就是4
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries) - 1):
            result += min(duration, timeSeries[i + 1] - timeSeries[i])
        return result + duration

solution = Solution()
print(solution.findPoisonedDuration(timeSeries = [1,4], duration = 2))
print(solution.findPoisonedDuration(timeSeries = [1,2], duration = 2))
print(solution.findPoisonedDuration(timeSeries = [1,2,5], duration = 2))