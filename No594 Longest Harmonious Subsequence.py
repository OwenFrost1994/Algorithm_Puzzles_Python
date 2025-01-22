# 计数类问题
from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mxl = 0
        for n in nums:
            if n + 1 in nums:
                mxl = max(mxl, cnt[n] + cnt[n + 1])
        return mxl

solution = Solution()
print(solution.findLHS(nums = [1,3,2,2,5,2,3,7]))
print(solution.findLHS(nums = [1,2,3,4]))
print(solution.findLHS(nums = [1,1,1,1]))