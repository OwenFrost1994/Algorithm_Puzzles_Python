# https://leetcode.com/problems/increasing-triplet-subsequence/solutions/3549612/python-easy-solution/
from typing import List
from math import inf
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf, inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

solution = Solution()
print(solution.increasingTriplet(nums = [1,2,3,4,5]))
print(solution.increasingTriplet(nums = [5,4,3,2,1]))
print(solution.increasingTriplet(nums = [2,1,5,0,4,6]))