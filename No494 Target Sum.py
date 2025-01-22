# 可以等效成从sum里面减去2倍的某些数值达到target,这样如果nums的和小于target或者sum-target不能被2整除就不能找到
# n是一共要减去多少，看着有几种方法从里面减少 dp[n + 1] dp[0]代表不减去任何数，也就是1
# dp求解的是减去多少数正好够减去n，每次从sum里面减去一个数值num，都是dp在dp[i - num]的方案个数叠加到dp[i]
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s - target) % 2 != 0:
            return 0
        n = (s - target) // 2 
        dp = [0]*(n + 1)
        dp[0] = 1
        for num in nums:
            for i in range(n, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]

solution = Solution()
print(solution.findTargetSumWays(nums = [1], target = 1))
print(solution.findTargetSumWays(nums = [1,1,1,1,1], target = 3))
