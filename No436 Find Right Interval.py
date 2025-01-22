# 一个排序类问题，排序的方法是看第二个值，后一个是不是有比前面小的
# 因为排序以后值直接乱序了,所以处理是给每一个子区间加一个index
from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals = sorted(intervals, key = lambda x: x[0])
        results = [-1] * n
        for _, e, i in intervals:
            j = bisect_left(intervals, [e])
            if j < n:
                results[i] = intervals[j][2]
        return results

solution = Solution()
print(solution.findRightInterval([[1,2]]))
print(solution.findRightInterval([[3,4],[2,3],[1,2]]))
print(solution.findRightInterval([[1,4],[2,3],[3,4]]))
