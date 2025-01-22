# the no duplicate array is
# [1 2 3 4 5 6 .... n]
#  0 1 2 3 4 5 .... n-1

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [v for i, v in enumerate(nums) if v != i + 1]

solution = Solution()
print(solution.findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(solution.findDuplicates(nums = [1,1,2]))
print(solution.findDuplicates(nums = [1]))