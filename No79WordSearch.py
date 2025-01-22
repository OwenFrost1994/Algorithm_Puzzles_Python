from collections import Counter
class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        if len(word) > m*n:
            return False
        
        count = Counter(sum(board, []))

        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]

        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))  #backtracking
            
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(solution.exist(board, word))

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(solution.exist(board, word))