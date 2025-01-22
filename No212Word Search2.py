from collections import Counter
# class Solution:
#     def findWords(self, board, words):
#         m = len(board)
#         n = len(board[0])

#         validwords = []
#         count = {}

#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] not in count.keys():
#                     count[board[i][j]] = []
#                     count[board[i][j]].append([i,j])
#                 else:
#                     count[board[i][j]].append([i,j])

#         for word in words:
#             isvalid = 1
#             for letter, num in Counter(word).items():
#                 if letter not in count.keys() or len(count[letter]) < num:
#                     isvalid = 0
#                     break
#             if len(word) <= m*n and isvalid == 1:
#                 validwords.append(word)
        
#         if len(validwords) == 0:
#             return []
        
#         def dfs(i , j , index, word):
#             if index == len(word):
#                 return True
#             if [i, j] in seen or i >= m or j >= n or i < 0 or j < 0 or board[i][j] != word[index]:
#                 return False
            
#             seen.append([i, j])
#             found = dfs(i + 1, j, index + 1, word) or dfs(i - 1, j, index + 1, word) or dfs(i, j + 1, index + 1, word) or dfs(i, j - 1, index + 1, word)
#             seen.remove([i, j])
#             return found
        
#         result = []
#         for word in validwords:
#             for point in count[word[0]]:
#                 seen = []
#                 if dfs(point[0], point[1], 0, word):
#                     result.append(word)
#                     break
        
#         return result

class Solution:
    def findWords(self, board, words):
        
        # Define a DFS function to traverse the board and search for words
        def dfs(x, y, root):
            # Get the letter at the current position on the board
            letter = board[x][y]
            # Traverse the trie to the next node
            cur = root[letter]
            # Check if the node has a word in it
            word = cur.pop('#', False)
            if word:
                # If a word is found, add it to the results list
                res.append(word)
            # Mark the current position on the board as visited
            board[x][y] = '*'
            # Recursively search in all four directions
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                # Check if the next position is within the board and the next letter is in the trie
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            # Restore the original value of the current position on the board
            board[x][y] = letter
            # If the current node has no children, remove it from the trie
            if not cur:
                root.pop(letter)
                
        # Build a trie data structure from the list of words
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Initialize a list to store the results
        res = []
        
        # Traverse the board and search for words
        for i in range(m):
            for j in range(n):
                # Check if the current letter is in the trie
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        # Return the list of results
        return res
    
solution = Solution()

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# print(solution.findWords(board, words))

# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# print(solution.findWords(board, words))

board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
print(solution.findWords(board, words))