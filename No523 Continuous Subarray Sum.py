# 这个题还是暴力求解，但是高手写的非常屌，他用了dict来记录前面的求和和求和的个数，取模来记录
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        mp = {0: -1}
        for i, v in enumerate(nums):
            s += v
            r = s % k
            if r in mp and i - mp[r] >= 2:
                return True
            if r not in mp:
                mp[r] = i
        return False