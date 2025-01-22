# 这个特殊在需要记录搜索路径，每次都从最上面一行开始螺旋搜索，每一个相同的搜索路径对应一个相同的形状也就一个相似岛屿
# 记录搜索过程可以不用辅助visited，可以直接修改原array
# 不知道为什么需要path.append("+" + direct)记录返回的路径才能区别有的形状
from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, direct, path):
            path.append(direct)
            grid[x][y] = 0
            for dx, dy in directs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny, "(" + str(dx) + "," + str(dy) + ")", path)
            path.append("+" + direct)

        m = len(grid)
        n = len(grid[0])
        directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        island = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, "s", path)
                    island.add("-".join(path))
        return len(island)

solution = Solution()
print(solution.numDistinctIslands(grid = [[0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],[0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],[1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]))
print(solution.numDistinctIslands(grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(solution.numDistinctIslands(grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))