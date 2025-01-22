from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        result = 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 0
        return max(result, cnt)
    
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))
