# A special DP solution. For dp matrix, ith row means the num[i] added into the set. The jth column
# means the value reached or not by add several numbes. For jth column, dp[i][j] is True if dp[i-1][j]
# is True, because num[:i-1] entries are included then adding num[i] is also True. dp[i][0] must be True,
# since including nothing results in reaching zero. If dp[i - 1][j - num[v]] is True when j - num[v] >= 0,
# then dp[i][j] must be True.
# the loop of j must go reversely such that one number is used for once.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        n = sum(nums) // 2
        dp = [[False] * (n + 1)for _ in range(len(nums))]
        dp[0][0] = True
        for i in range(0, len(nums)):
            for j in range(n, -1, -1):
                if i == 0:
                    if j - nums[i] >= 0:
                        dp[i][j] = dp[i][j - nums[i]]
                else:
                    if j - nums[i] >= 0:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

solution = Solution()
print(solution.canPartition(nums = [1,5,10,6]))
print(solution.canPartition(nums = [3,3,3,4,5]))
print(solution.canPartition(nums = [1,5,11,5]))
print(solution.canPartition(nums = [1,2,3,5]))