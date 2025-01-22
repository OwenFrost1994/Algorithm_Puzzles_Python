from math import inf
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        min2 = - inf
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min2:
                return True
            while stack and stack[-1] < nums[i]:
                min2 = stack.pop()
            stack.append(nums[i])
        return False
    
class Solution2:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min2 = - inf
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < min2:
                return True
            while stack and stack[-1] < nums[i]:
                if stack[-1] > min2:
                    min2 = stack.pop()
                else:
                    stack.pop()
            stack.append(nums[i])
        return False
solution = Solution()
print(solution.find132pattern(nums = [1,2,3,4]))
print(solution.find132pattern(nums = [3,1,4,2]))
print(solution.find132pattern(nums = [-1,3,2,0]))
