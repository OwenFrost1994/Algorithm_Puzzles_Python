from math import inf
class Solution:
    def minCost(self, costs) -> int:
        n = len(costs)
        m = len(costs[0])
        dp = [[0]*m + [inf] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m):
                dp[i][j] = costs[i - 1][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])
        return min(dp[-1])

solution = Solution()
print(solution.minCost([[17,2,17],[16,16,5],[14,3,19]]))
print(solution.minCost([[7,6,2]]))