# dfs is not hard for me lets try union find method

from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for a, b in edges:
            p[find(a)] = find(b)
        return sum(i == find(i) for i in range(n)) # or len(set(parents))

solution = Solution()
print(solution.countComponents(n = 5, edges = [[0, 1], [1, 2], [3, 4]]))
print(solution.countComponents(n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]))