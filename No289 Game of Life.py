class Solution:
    def gameOfLife(self, board) -> None:
        def withinbounds(a, b):
            if a >= 0 and a < len(board) and b >= 0 and b < len(board[0]):
                return True
            else:
                return False
            
        def neighbours(i, j):
            n = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:
                        continue
                    if withinbounds(i+a, j+b):
                        n.append(board[i+a][j+b])
            return n
        
        liveneighbor = [[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveneighbor[i][j] = sum(neighbours(i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = liveneighbor[i][j]
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1
        return board
    
solution = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(solution.gameOfLife(board))

board = [[1,1],[1,0]]
print(solution.gameOfLife(board))