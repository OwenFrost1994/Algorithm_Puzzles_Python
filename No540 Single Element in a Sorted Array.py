# 因为只有一个重复，需要找重复的在哪，就是一个二分搜索
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if (mid % 2 == 0 and nums[mid] != nums[mid + 1]) or (mid % 2 == 1 and nums[mid] != nums[mid - 1]):
                r = mid
            else:
                l = mid + 1
        return nums[l]

solution = Solution()
print(solution.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))
print(solution.singleNonDuplicate(nums = [3,3,7,7,10,11,11]))