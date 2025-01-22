class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = n*[0]
        dp[0] = 1
        x=0
        y=0
        z=0
        for i in range(1, n):
            dp[i] = min(dp[x]*2, min(dp[y]*3, dp[z]*5))
            if dp[i] == 2*dp[x]:
               x += 1
            if dp[i] == 3*dp[y]:
               y += 1
            if dp[i] == 5*dp[z]:
                z += 1
        return dp[n-1]

solution = Solution()
n = 10
print(solution.nthUglyNumber(n))

n = 1
print(solution.nthUglyNumber(n))