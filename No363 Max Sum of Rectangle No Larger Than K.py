# the idea from "Range Sum Query 2D-Immutable" is used, the a sum matrix store the sum from (0, 0) to (i, j)
from typing import List
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = float("-inf")
        dp = [[0] * n for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
        for start in range(0, n):
            for end in range(start, n):
                sums = [0]
                subsum = 0
                for i in range(m):
                    if start > 0:
                        subsum += dp[i][end] - dp[i][start - 1]
                    else:
                        subsum += dp[i][end]
                    idx = bisect.bisect_left(sums, subsum - k)
                    if idx < len(sums):
                        ans = max(ans, subsum - sums[idx])
                    bisect.insort(sums, subsum)
        return ans

solution = Solution()
print(solution.maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2))
print(solution.maxSumSubmatrix(matrix = [[2,2,-1]], k = 3))
