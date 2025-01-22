class Solution:
    def getFactors(self, n: int):
        ans = []

        def dfs(n, s, path):
            if n <= 1:
                if len(path) > 1:
                    ans.append(path.copy())
                return
            
            for i in range(s, n + 1):
                if n % i == 0:
                    path.append(i)
                    dfs(n//i, i, path)
                    path.pop()
            return
        dfs(n, 2, [])
        return ans

solution = Solution()
print(solution.getFactors(1))
print(solution.getFactors(12))
print(solution.getFactors(37))