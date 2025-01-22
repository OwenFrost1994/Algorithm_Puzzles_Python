# 经典sliding window法， 统计其中零的个数

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        k = 1
        result = 0
        zero = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            while zero > k:
                if nums[l] == 0:
                    zero -= 1
                l += 1
                
            result = max(result, r - l + 1)
            r += 1
            
        return result

solution = Solution()
print(solution.findMaxConsecutiveOnes(nums = [1,0,1,1,0]))
print(solution.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))
