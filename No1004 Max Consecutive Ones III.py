from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
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
print(solution.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(solution.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
