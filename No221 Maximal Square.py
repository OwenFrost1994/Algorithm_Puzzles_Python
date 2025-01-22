class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0]*(m+1) for _ in range(n+1)]
        max_side = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    max_side = max(max_side, dp[i + 1][j + 1])
        return max_side * max_side

solution = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

print(solution.maximalSquare(matrix))