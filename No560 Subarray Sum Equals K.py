from collections import Counter
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        mp = Counter({0:1})
        s = 0
        for num in nums:
            s += num
            result += mp[s - k]
            mp[s] += 1
        return result


solution = Solution()
print(solution.subarraySum(nums = [1], k = 0))
print(solution.subarraySum(nums = [1,1,1], k = 2))
print(solution.subarraySum(nums = [1,2,3], k = 3))