class Solution:
    gsearched = [[]]
    gboard = [[]]
    def solve(self, board):
        self.gsearched = [[False]*len(board[0]) for _ in range(len(board))]
        self.gboard = board
        j = 0
        for i in range(0, len(board)):
            if board[i][j] == "O" and self.gsearched[i][j] == False:
                self.dfs(i ,j)
        j = len(board[0]) - 1
        for i in range(0, len(board)):
            if board[i][j] == "O" and self.gsearched[i][j] == False:
                self.dfs(i ,j)
        
        i = 0
        for j in range(0, len(board[0])):
            if board[i][j] == "O" and self.gsearched[i][j] == False:
                self.dfs(i ,j)
        i = len(board) - 1
        for j in range(0, len(board[0])):
            if board[i][j] == "O" and self.gsearched[i][j] == False:
                self.dfs(i ,j)
        
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O" and self.gsearched[i][j] == False:
                    board[i][j] = "X"
        return board
    
    def dfs(self, i ,j):
        if i < 0 or i >= len(self.gboard) or j < 0 or j >= len(self.gboard[0]):
            return
        if self.gboard[i][j] == "O" and self.gsearched[i][j] == False:
            # print(self.gsearched[i][j])
            self.gsearched[i][j] = True
            self.dfs(i + 1, j)
            self.dfs(i - 1, j)
            self.dfs(i, j + 1)
            self.dfs(i, j - 1)
        else:
            return

solution = Solution()
board = [["X","X","O","X","X","O","X","O"],["X","X","X","O","X","X","O","X"],["X","X","X","O","X","O","X","O"],["O","X","X","X","X","O","O","X"],["O","O","O","X","O","O","O","X"],["O","X","O","O","X","X","O","X"],["O","X","O","O","X","O","X","X"],["O","X","X","X","O","O","O","X"]]
print(solution.solve(board))
solution = Solution()
board = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
print(solution.solve(board))

solution = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solution.solve(board))

board = [["X"]]
print(solution.solve(board))

board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
print(solution.solve(board))