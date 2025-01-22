from typing import List
# dp method, calculate how many enemies from left to right. When meet a wall, reset variable to zero
# same for right to left
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            t = 0
            for j in range(n):
                if grid[i][j] == "E":
                    t += 1
                elif grid[i][j] == "W":
                    t = 0
                else:
                    dp[i][j] += t
            t = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "E":
                    t += 1
                elif grid[i][j] == "W":
                    t = 0
                else:
                    dp[i][j] += t
        for j in range(n):
            t = 0
            for i in range(m):
                if grid[i][j] == "E":
                    t += 1
                elif grid[i][j] == "W":
                    t = 0
                else:
                    dp[i][j] += t
            t = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == "E":
                    t += 1
                elif grid[i][j] == "W":
                    t = 0
                else:
                    dp[i][j] += t
        return max([max(dp[i]) for i in range(m)])

solution = Solution()
print(solution.maxKilledEnemies(grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))
print(solution.maxKilledEnemies(grid = [["W","W","W"],["0","0","0"],["E","E","E"]]))