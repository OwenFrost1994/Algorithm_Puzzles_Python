# 这个不是找能不能到，而是能不能停住，同时要有一个来记录走的方法，也就是每一个位置还有记录走法的array
from collections import deque
from math import inf
from typing import List

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        nodes = deque()
        nodes.append(ball)
        direct = [[-1, 0, "u"], [0, 1, "r"], [1, 0, "d"], [0, -1, "l"]]
        dist = [[inf] * n for _ in range(m)]
        dist[ball[0]][ball[1]] = 0
        paths = [[None] * n for _ in range(m)]
        paths[ball[0]][ball[1]] = ""
        while nodes:
            node = nodes.popleft()
            path = paths[node[0]][node[1]]
            for a, b, p in direct:
                x, y, step = node[0] , node[1], dist[node[0]][node[1]]
                while 0 <= x + a < m and 0 <= y + b < n and maze[x + a][y + b] != 1 and (x != hole[0] or y != hole[1]): #防止小球出来
                    x, y, step = x + a, y + b, step + 1
                if dist[x][y] > step or (dist[x][y] == step and path + p < paths[x][y]): # 找最短距离里面字典最小的
                    dist[x][y] = step
                    paths[x][y] = path + p
                    if x != hole[0] or y != hole[1]: #已经进了就不行了
                        nodes.append([x, y])
        return paths[hole[0]][hole[1]] or "impossible" 

solution = Solution()
print(solution.findShortestWay(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], ball = [0,4], hole = [1,2]))
print(solution.findShortestWay(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], ball = [0,4], hole = [4,4]))
print(solution.findShortestWay(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], ball = [0,4], hole = [3,2]))