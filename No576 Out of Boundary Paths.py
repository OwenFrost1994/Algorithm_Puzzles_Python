class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # @__cached__
        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            if k == 0:
                return 0
            res = 0
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                res += dfs(i + a, j + b, k - 1)
                res = res % (10**9 + 7 + 7)
            return res
        return dfs(startRow, startColumn, maxMove)

solution = Solution()
print(solution.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(solution.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))