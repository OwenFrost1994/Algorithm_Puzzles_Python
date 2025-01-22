# 这个不能单指针法，必须双的
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result, s, j = 0, 1, 0
        for i, n in enumerate(nums):
            s *= n
            while j <= i and s >= k:
                s //= nums[j]
                j += 1
            result += i - j + 1
        return result

solution = Solution()
print(solution.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
print(solution.numSubarrayProductLessThanK(nums = [1,2,3], k = 0))