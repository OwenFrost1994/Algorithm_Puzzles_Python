# This is a typical search problem we can transversal every node to see if a node can reach both ocean
# Then the problem is a dfs (depth first search) problem
# but we can think reversely, search from the beach to see which nodes can flow into a ocean
# This transfer problem into bfs (breadth first search)

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i, j, visited):
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                I, J = i + x, j + y
                if 0 <= I < m and 0 <= J < n and heights[I][J] >= heights[i][j] and (I, J) not in visited:
                    visited.add((I, J))
                    bfs(I, J, visited)
            
        Pbeach = [] # starting node list
        Pacific = set()
        Abeach = [] # starting node list
        Atlantic = set()
        m, n = len(heights), len(heights[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    Pbeach.append((i, j))
                    Pacific.add((i, j))
                if i == m - 1 or j == n - 1:
                    Abeach.append((i, j))
                    Atlantic.add((i, j))
        for i, j in Pbeach:
            bfs(i, j, Pacific)
        for i, j in Abeach:
            bfs(i, j, Atlantic)
        return [[x, y] for x, y in Pacific & Atlantic]

solution = Solution()
print(solution.pacificAtlantic(heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print(solution.pacificAtlantic(heights = [[1]]))
