from math import inf
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        isVisited = [[False] * n for _ in range(m)]

        def dfs(i ,j, level):
            if i < 0 or i >= m  or j < 0 or j >= n:
                return
            if rooms[i][j] == -1 or isVisited[i][j] == True:
                return
            if level < rooms[i][j]:
                rooms[i][j] = level
            isVisited[i][j] = True
            for x, y in direct:
                dfs(i + x, j + y, level + 1)
            isVisited[i][j] = False

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j , 0)
                
        
solution = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
solution.wallsAndGates(rooms)
print(rooms)
rooms = [[-1]]
solution.wallsAndGates(rooms)
print(rooms)