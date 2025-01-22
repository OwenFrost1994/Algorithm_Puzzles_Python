class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        path = []
        for i in range(len(obstacleGrid)):
            path.append([0]*len(obstacleGrid[0]))
        isobstacle = 0
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                isobstacle = 1
            if isobstacle == 1:
                path[0][i] = 0
            else:
                path[0][i] = 1
        isobstacle = 0 
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                isobstacle = 1
            if isobstacle == 1:
                path[i][0] = 0
            else:
                path[i][0] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                path[i][j] = (1 - obstacleGrid[i-1][j])*path[i-1][j] + (1 - obstacleGrid[i][j-1])*path[i][j-1]
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
        return path[-1][-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))

obstacleGrid = [[0,1],[0,0]]
print(solution.uniquePathsWithObstacles(obstacleGrid))