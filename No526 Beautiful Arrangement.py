from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i):
            nonlocal result, visited
            if i == n + 1:
                result += 1
                return
            for j in match[i]:
                if not visited[j]:
                    visited[j] = True
                    dfs(i + 1)
                    visited[j] = False
            
        visited = [False] * (n + 1)
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    match[i].append(j)
        result = 0
        dfs(1)
        return result

solution = Solution()
print(solution.countArrangement(2))
print(solution.countArrangement(1)) 