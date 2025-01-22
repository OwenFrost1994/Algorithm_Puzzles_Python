from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(a, b, c, d):
            ones = 0
            zeros = 0
            for i in range(a, c):
                for j in range(b, d):
                    if grid[i][j] == 0:
                        zeros = 1
                    else:
                        ones = 1
            if zeros and ones:
                isLeaf = False
            else:
                isLeaf = True
            if not isLeaf:
                val = 1
            else:
                val = 1 if ones else 0
            if isLeaf:
                return Node(val, isLeaf, None, None, None, None)
            else:
                topLeft = dfs(a, b, (a + c)//2, (b + d)//2)
                topRight = dfs(a, (b + d)//2, (a + c)//2, d)
                bottomLeft = dfs((a + c)//2, b, c, (b + d)//2)
                bottomRight = dfs((a + c)//2, (b + d)//2, c, d)
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0,0,len(grid),len(grid[0]))
    
solution = Solution()
root = solution.construct(grid = [[0,1],[1,0]])
root = solution.construct(grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
