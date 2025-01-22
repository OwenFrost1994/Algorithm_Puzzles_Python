# 每一对都选最小的，那么那就得让两个数字尽可能接近，只有非常接近的数字才能最大化小的数字，这样的话就两个一对
# 本质是个排序问题
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
solution = Solution()
print(solution.arrayPairSum(nums = [1,4,3,2]))
print(solution.arrayPairSum(nums = [6,2,6,5,1,2]))