from collections import deque
from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        # numbers = "B123456789"
        m, n = len(board), len(board[0])
        q = deque([click])
        direct = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        while q:
            x, y = q.popleft()
            if board[x][y] == "B":
               continue
            mine = 0
            nbrs = []
            for dx, dy in direct:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in ["M", "E"]:
                    if board[nx][ny] == "M":
                        mine += 1
                    else:
                        nbrs.append([nx, ny])
            if mine == 0:
                q.extend(nbrs)
                board[x][y] = "B"
            else:
                board[x][y] = str(mine)
            # board[x][y] = numbers[mine]
        return board

solution = Solution()
print(solution.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))
print(solution.updateBoard(board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]))