from typing import List
from math import inf
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = len(costs[0])
        dp = [[0]*m + [inf] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m):
                dp[i][j] = costs[i - 1][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
        return min(dp[-1])

solution = Solution()
print(solution.minCostII([[17,2,17],[16,16,5],[14,3,19]]))
print(solution.minCostII([[1,5,3],[2,9,4]]))
print(solution.minCostII([[7,6,2]]))
print(solution.minCostII([[1,3],[2,4]]))