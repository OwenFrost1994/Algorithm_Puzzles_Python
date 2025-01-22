# 是个dp，但是必须考虑四个方向的dp

from typing import List

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(4)]
        result = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if mat[i - 1][j - 1] == 1:
                    dp[0][i][j] = dp[0][i - 1][j] + 1
                    dp[1][i][j] = dp[1][i][j - 1] + 1
                    dp[2][i][j] = dp[2][i - 1][j - 1] + 1
                    dp[3][i][j] = dp[3][i - 1][j + 1] + 1
                    result = max(result, dp[0][i][j], dp[1][i][j], dp[2][i][j], dp[3][i][j])
        return result

solution = Solution()
print(solution.longestLine(mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]))
print(solution.longestLine(mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]))