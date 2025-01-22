from functools import cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            ans = 1
            for a, b in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x, y = i + a, j + b
                if x >= 0 and x < m and y >=0 and y < n and matrix[x][y] < matrix[i][j]:
                    ans = max(ans, dfs(x, y) + 1)
            return ans
        m, n = len(matrix), len(matrix[0])
        return max(dfs(i, j) for i in range(m) for j in range(n))

solution = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(solution.longestIncreasingPath(matrix))
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(solution.longestIncreasingPath(matrix))
matrix = [[1]]
print(solution.longestIncreasingPath(matrix))