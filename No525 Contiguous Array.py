# 这个高在把0看成-1，找和为0的点，如果前面和不是0，如果这个和再出现一次，那就意味着在这之间存在一组和为0
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = ans = 0
        mp = {0: -1}
        for i, v in enumerate(nums):
            s += 1 if v == 1 else -1
            if s in mp:
                ans = max(ans, i - mp[s])
            else:
                mp[s] = i
        return ans


solution = Solution()
print(solution.findMaxLength(nums = [0,1]))
print(solution.findMaxLength(nums = [0,1,0]))