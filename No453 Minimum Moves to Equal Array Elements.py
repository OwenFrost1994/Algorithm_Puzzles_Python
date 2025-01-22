# 将n - 1 个元素递增1 相当于将所有元素递增 1，并将一个元素递减 1。
# 由于将所有元素递增 1 不会改变元素是否相等，因此该过程相当于仅将一个元素递减 1。
# 有一个平衡服务器脆弱性的问题是一样的

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)

solution = Solution()
print(solution.minMoves(nums = [1,2,3]))
print(solution.minMoves(nums = [1,1,1]))