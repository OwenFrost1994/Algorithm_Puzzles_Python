from collections import defaultdict
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        result = 0
        for num in mp:
            if k == 0:
                if mp[num] > 1:
                    result += 1
            else:
                if num + k in mp:
                    result += 1
        return result
solution = Solution()
print(solution.findPairs(nums = [3,1,4,1,5], k = 2))
print(solution.findPairs(nums = [1,2,3,4,5], k = 1)) 