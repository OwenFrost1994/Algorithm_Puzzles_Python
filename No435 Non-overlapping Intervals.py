import math
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        point = -math.inf

        intervals = sorted(intervals, key = lambda x:x[1])
        for interval in intervals:
            if point <= interval[0]:
                point = interval[1]
            else:
                ans += 1
        return ans
solution = Solution()
print(solution.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
print(solution.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(solution.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))