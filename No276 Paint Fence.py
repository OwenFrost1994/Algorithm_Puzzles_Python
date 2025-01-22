class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = k
        for i in range(1, n):
            dp[i][0] = (k - 1)*(dp[i - 1][0] + dp[i - 1][1]) #different colors
            dp[i][1] = dp[i - 1][0] #same colors
        return sum(dp[-1])

solution = Solution()
print(solution.numWays(n = 1, k = 1))
print(solution.numWays(n = 2, k = 1))
print(solution.numWays(n = 2, k = 2))
print(solution.numWays(n = 7, k = 2))
print(solution.numWays(n = 7, k = 4))