# https://leetcode.ca/2016-10-22-327-Count-of-Range-Sum/
from typing import List
import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        def update(b, i, delta):
            while i < len(b):
                b[i] += delta
                i += (i & -i)

        def sumRange(b, i):
            ret = 0
            while i > 0:
                ret += b[i]
                i -= (i & -i)
            return ret

        ans = 0
        pres = [0] * (len(nums) + 1)
        b = [0] * (len(nums) + 2)

        for i in range(0, len(nums)):
            pres[i + 1] = pres[i] + nums[i]

        sortedPres = sorted(pres)

        for end in pres:
            count = sumRange(b, bisect.bisect_right(sortedPres, end - lower)) - sumRange(b, bisect.bisect_left(sortedPres,
                                                                                                            end - upper))
            ans += count
            update(b, bisect.bisect_left(sortedPres, end) + 1, 1)
        return ans
    
solution = Solution()
print(solution.countRangeSum(nums = [-2,5,-1], lower = -2, upper = 2))
print(solution.countRangeSum(nums = [0], lower = 0, upper = 0))