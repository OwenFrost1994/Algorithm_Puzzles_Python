# A special DP solution. dp[i][d] store the number of subsequence reaching i with the same differences d.
# And the subsequence here is the subsequnce with length 2
# for qick indexing, use list[i] = dict{difference: num of difference} to store the number of subsequence before i and has the same
# differences d.
# we need to know that for j that j < i, we have list[j][d] subsquence at least length is 2, then for list[i][d] we have 1 + list[j][d]
# because subsequnce with length >= 2 add i is still a subsequence with length >= 2
# and for results need subsquence >= 3, result += list[j][d]
import collections
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in nums]
        result = 0
        for i in range(len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] += 1
                if d in dp[j]:
                    dp[i][d] += dp[j][d]
                    result += dp[j][d]
        return result

solution = Solution()
print(solution.numberOfArithmeticSlices(nums = [2,4,6,8,10]))
print(solution.numberOfArithmeticSlices(nums = [7,7,7,7,7]))