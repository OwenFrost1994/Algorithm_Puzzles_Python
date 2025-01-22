class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        result = []
        self.dfs(dungeon, 0, 0, 0, 0, result)
        return min(result)
    def dfs(self, dungeon, i, j, minlife, currlife, result):
        currlife = currlife + dungeon[i][j]
        if  currlife < minlife:
            minlife = currlife
        if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
            result.append(abs(minlife) + 1)
            return
        
        if i + 1 < len(dungeon):
            self.dfs(dungeon, i + 1, j, minlife, currlife, result)
        if j + 1 < len(dungeon[0]):
            self.dfs(dungeon, i, j + 1, minlife, currlife, result)

class Solution1:
    def calculateMinimumHP(self, dungeon) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]
    
solution = Solution1()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(solution.calculateMinimumHP(dungeon))