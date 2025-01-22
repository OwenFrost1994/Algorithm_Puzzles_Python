from typing import List
# here we use dp method
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]

solution = Solution()
print(solution.combinationSum4(nums = [1,2,3], target = 4))
print(solution.combinationSum4(nums = [9], target = 3))