from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if i > 0 and board[i - 1][j] == "X":
                        continue
                    elif j > 0 and board[i][j - 1] == "X":
                        continue
                    result += 1
        return result

solution = Solution()
print(solution.countBattleships(board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(solution.countBattleships(board = [["."]]))