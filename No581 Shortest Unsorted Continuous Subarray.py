from math import inf
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mi, mx = inf, -inf
        l = r = -1
        n = len(nums)
        for i, x in enumerate(nums):
            if mx > x:
                r = i
            else:
                mx = x
            if mi < nums[n - i - 1]:
                l = n - i - 1
            else:
                mi = nums[n - i - 1]
        return 0 if r == -1 else r - l + 1

solution = Solution()
print(solution.findUnsortedSubarray(nums = [2,6,4,8,10,9,15]))
print(solution.findUnsortedSubarray(nums = [1,2,3,4]))