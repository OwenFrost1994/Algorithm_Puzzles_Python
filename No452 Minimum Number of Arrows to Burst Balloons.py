# 也是一个排序问题，找有没有在一起的interva
from math import inf
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x: x[1])
        pointer = -inf
        result = 0
        for i in range(n):
            if points[i][0] > pointer:
                pointer = points[i][1]
                result += 1
        return result

# points = [[1, 4], [1, 3], [1, 2], [2, 3], [2, 4]]
# print(points.sort())
solution = Solution()
print(solution.findMinArrowShots(points = [[1, 4], [1, 3], [1, 2], [2, 3], [2, 4]]))
print(solution.findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print(solution.findMinArrowShots(points = [[1,2],[3,4],[5,6],[7,8]]))
print(solution.findMinArrowShots(points = [[1,2],[2,3],[3,4],[4,5]]))