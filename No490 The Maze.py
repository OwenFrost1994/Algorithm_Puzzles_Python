# 用dfs我感觉效率不高，用bfs试试吧
# 这个不是找能不能到，而是能不能停住，也就是连续不停的往前走到墙边看有没有destination
# 这三个题理解大错心态放弃就在于没有考虑直接走到头，可以看成一个dfs+bfs，考虑好前进的条件
from collections import deque
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        nodes = deque()
        nodes.append(start)
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while nodes:
            node = nodes.popleft()
            visited.add((node[0], node[1]))
            for a, b in direct:
                x, y = node[0] , node[1] 
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] != 1:
                    x, y = x + a, y + b
                if x == destination[0] and y == destination[1]:
                    return True
                if (x, y) not in visited:
                    nodes.append([x, y])
        return False

solution = Solution()
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [1,2]))
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]))
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]))
