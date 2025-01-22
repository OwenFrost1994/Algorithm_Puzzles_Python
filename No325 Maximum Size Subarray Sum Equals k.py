# https://leetcode.ca/2016-10-20-325-Maximum-Size-Subarray-Sum-Equals-k/
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mp = {0:-1}
        s = result = 0
        for i, v in enumerate(nums):
            s += v
            if s - k in mp:
                result = max(result, i - mp[s - k])
            if s not in mp:
                mp[s] = i
        return result

solution = Solution()
print(solution.maxSubArrayLen(nums = [1,-1,5,-2,3], k = 3))
print(solution.maxSubArrayLen(nums = [-2,-1,2,1], k = 1))