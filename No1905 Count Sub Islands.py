# 我一开始想法是grid1的岛一个list(set())，然后搜索grid2的岛list(set())，二者求交，但是实际上没有必要
# 因为只要grid2的岛都在grid1的等于1的点,那grid2的岛就是1的子岛
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y, path):
            path.append([x, y])
            grid2[x][y] = 0
            for dx, dy in directs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
                    dfs(nx, ny, path)
        
        m = len(grid2)
        n = len(grid2[0])
        directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        islands = []
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    path = []
                    dfs(i, j, path)
                    islands.append(path)
        results = 0
        for island in islands:
            result = 1
            for i, j in island:
                if grid1[i][j] != 1:
                    result = 0
                    break
            results += result
        return results

# 这里高手写的间接的多
        # def dfs(i, j):
        #     ans = grid1[i][j] == 1
        #     grid2[i][j] = 0
        #     for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
        #         x, y = i + a, j + b
        #         if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1 and not dfs(x, y):
        #             ans = False
        #     return ans

        # m, n = len(grid1), len(grid1[0])
        # return sum(grid2[i][j] == 1 and dfs(i, j) for i in range(m) for j in range(n))
solution = Solution()
print(solution.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
                                   grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))
print(solution.countSubIslands(grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
                                   grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))
