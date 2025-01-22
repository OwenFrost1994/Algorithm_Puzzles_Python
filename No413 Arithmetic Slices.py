from math import inf
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        d = inf
        count = 0
        for i in range(1,len(nums)):
            a, b = nums[i-1], nums[i]
            if b - a == d:
                count += 1
            else:
                count = 0
                d = b - a
            result += count
        return result

solution = Solution()
print(solution.numberOfArithmeticSlices(nums = [1,2,3,4]))
print(solution.numberOfArithmeticSlices(nums = [1,2,3,8,9,10]))
print(solution.numberOfArithmeticSlices(nums = [1]))