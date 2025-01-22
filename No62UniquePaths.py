
class Solution:
    num = 0
    def uniquePaths(self, m, n):
        self.num = 0
        point = [0,0]
        self.path(m, n, point)
        return self.num
    def path(self, m , n, point):
        if point[0] == m - 1 and point[1] == n - 1:
            self.num += 1
            return
        
        if point[0] < m - 1:
            point[0] = point[0] + 1
            self.path(m, n, point)
            point[0] = point[0] - 1
        if point[1] < n - 1:
            point[1] = point[1] + 1
            self.path(m, n, point)
            point[1] = point[1] - 1
import math     
class Solution1:
    num = 0
    def uniquePaths(self, m, n):
        return math.comb(m+n-2, m-1)
    
class Solution2:
    def uniquePaths(self, m, n):
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]

m = 3
n = 7
solution = Solution2()
print(solution.uniquePaths(m, n))

m = 3
n = 2
print(solution.uniquePaths(m, n))