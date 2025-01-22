# 这个不是找能不能到，而是能不能停住，也就是连续不停的往前走到墙边看有没有destination
# 我们不管路径中间的点，只管撞墙的那些
from collections import deque
from math import inf
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        n = len(maze[0])
        nodes = deque()
        nodes.append(start)
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        dist = [[inf] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        while nodes:
            node = nodes.popleft()
            for a, b in direct:
                x, y, step = node[0] , node[1], dist[node[0]][node[1]]
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] != 1:
                    x, y, step = x + a, y + b, step + 1
                if dist[x][y] > step:
                    dist[x][y] = step
                    nodes.append([x, y])
        return -1 if dist[destination[0]][destination[1]] == inf else dist[destination[0]][destination[1]] 

solution = Solution()
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [1,2]))
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]))
print(solution.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]))