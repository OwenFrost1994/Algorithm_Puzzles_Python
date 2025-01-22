# 双指针法或者dfs，这里用dfs实现
from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, arr):
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if len(arr) == 0 or arr[-1] <= nums[i]:
                    arr.append(nums[i])
                    if len(arr) > 1 and arr not in result:
                        result.append(arr.copy())
                    dfs(i + 1, arr)
                    arr.pop()
        result = []
        dfs(0, [])
        return result

solution = Solution()
print(solution.findSubsequences(nums = [4,6]))
print(solution.findSubsequences(nums = [4,6,7]))
print(solution.findSubsequences(nums = [4,6,7,7]))
print(solution.findSubsequences(nums = [4,4,3,2,1]))
print(solution.findSubsequences(nums = [4,4,3,1]))