class Solution:
    def minSteps(self, n: int) -> int:
        # @cache
        def dfs(n):
            if n == 1:  
                return 0
            i = 2
            result = n # the worst case is we need n times
            while i*i <= n: # test from minimum operations, at least one copy and paste
                if n % i == 0:
                    result = min(result, dfs(n//i) + i)
                i += 1
            return result
        return dfs(n)


solution = Solution()
print(solution.minSteps(1))
print(solution.minSteps(3))