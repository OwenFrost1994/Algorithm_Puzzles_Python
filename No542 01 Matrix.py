# this is a bfs
from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        m, n = len(mat), len(mat[0])
        results = [[-1]*n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    results[i][j] = 0
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for a, b in d:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and results[x][y] == -1:
                    results[x][y] = results[i][j] + 1
                    q.append((x, y))
        return results
solution = Solution()
print(solution.updateMatrix([[0,0,1,0,1,1,1,0,1,1],[1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,1,1],[1,0,1,0,1,1,1,0,1,1],[0,0,1,1,1,0,1,1,1,1],[1,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,1,1],[1,1,1,0,1,1,0,1,0,1],[1,0,1,1,1,0,1,1,1,0]]))
print(solution.updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]]))
print(solution.updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]]))