# 这里单调堆存放的不是数而是存放index，通过index看是不是出现了最大值
# 环形队列一定存在最大值，只要走2n就行
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        results = [-1]*n
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i % n]:
                results[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return results

solution = Solution()
print(solution.nextGreaterElements(nums = [1,2,1]))
print(solution.nextGreaterElements(nums = [1,2,3,4,3]))
