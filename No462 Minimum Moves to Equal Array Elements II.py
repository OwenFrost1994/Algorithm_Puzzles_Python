# 解决办法是让所有数组元素等于数组的中位数。数组的中位数计算如下。如果数组的长度是奇数，那么中间的元素就是中位数。
# 如果数组的长度是偶数，那么中间两个元素的平均值就是中位数。
# 事实上，如果数组的长度是偶数，则中间两个元素之间的任何数字都可以被视为中位数，并且将导致移动次数最少。
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        k = nums[len(nums) >> 1]
        return sum(abs(v - k) for v in nums)
    
solution = Solution()
print(solution.minMoves2(nums = [1,2,3]))
print(solution.minMoves2(nums = [1,10,2,9]))