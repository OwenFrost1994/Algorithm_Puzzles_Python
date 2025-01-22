from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key = lambda x: x[-1])
        maxval = 0
        maximum = arrays[0][-1]
        minmum = arrays[0][0]
        for i in range(1, len(arrays)):
            maxval = max(maxval, abs(arrays[i][-1] - minmum), abs(maximum - arrays[i][0]))
            maximum = max(maximum, arrays[i][-1])
            minmum = min(minmum, arrays[i][0])
        return maxval

solution = Solution()
print(solution.maxDistance(arrays = [[1,4,5],[0,2]]))
print(solution.maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]]))
print(solution.maxDistance(arrays = [[1],[1]]))
print(solution.maxDistance(arrays = [[-2],[-3,-2,1]]))