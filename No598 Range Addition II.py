from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i, j in ops:
            m = min(m, i)
            n = min(n, j)
        return m * n

solution = Solution()
print(solution.maxCount(3, 3, [[2,2],[3,3]]))
print(solution.maxCount(4, 4, [[2,2],[3,3],[4,4],[1,1]]))
print(solution.maxCount(6, 2, [[1,2],[4,2],[3,1],[2,1]]))