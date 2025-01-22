from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 4
                    if i < m - 1 and grid[i + 1][j] == 1:
                        result -= 2
                    if j < n - 1 and grid[i][j + 1] == 1:
                        result -= 2
        return result

solution = Solution()
print(solution.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(solution.islandPerimeter(grid = [[1]]))
print(solution.islandPerimeter(grid = [[1,0]]))