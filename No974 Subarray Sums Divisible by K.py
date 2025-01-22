# 余数a再次出现意味着上次出现a和这次出现a中间的数的和可以被k整除，但是要加了这一次以后再加1
from collections import Counter
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = Counter({0: 1})
        result, s = 0, 0
        for n in nums:
            s = (s + n) % k
            result += mp[s]
            mp[s] += 1
        return result

solution = Solution()
print(solution.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
print(solution.subarraysDivByK(nums = [5], k = 9))