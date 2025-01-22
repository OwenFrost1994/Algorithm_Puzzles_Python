# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         if endWord not in wordList:
#             return 0
#         used = [0]*(len(wordList) + 1)
#         used[0] = 1
#         isone = [[0]*(len(wordList)+ 1) for i in range(len(wordList) + 1)]
#         for i in range(len(wordList) + 1):
#             for j in range(i + 1, len(wordList) + 1):
#                 if i == 0 or j == 0:
#                     isone[i][j] = self.isonedigit(beginWord, wordList[j - 1])
#                 else:
#                     isone[i][j] = self.isonedigit(wordList[i - 1], wordList[j - 1])
#                 isone[j][i] = isone[i][j]

#         return self.dfs(isone, wordList, used, endWord, 1, 0)
    
#     def dfs(self, isone, wordList, used, endWord, step, index):
#         if index > 0 and wordList[index - 1] == endWord:
#             return step
#         if sum(used) == len(wordList) + 1:
#             return len(wordList)
        
#         minmumstep = len(wordList) + 1
#         for i in range(1, len(wordList) + 1):
#             if used[i] == 0 and isone[index][i] == 1:
#                 used[i] = 1
#                 minmumstep = min(minmumstep, self.dfs(isone, wordList, used, endWord, step + 1, i))
#                 used[i] = 0
#         return minmumstep
        
#     def isonedigit(self, s, t):
#         for i in range(len(s)):
#             if s[i] == t[i]:
#                 i += 1
#             else:
#                 if s[i + 1:] == t[i + 1:]:
#                     return 1
#                 else:
#                     return 0
#         return 0

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        self.results = []
        if endWord not in wordList:
            return 0
        used = [0]*(len(wordList) + 1)
        used[0] = 1
        isone = [[0]*(len(wordList)+ 1) for i in range(len(wordList) + 1)]
        for i in range(len(wordList) + 1):
            for j in range(i + 1, len(wordList) + 1):
                if i == 0 or j == 0:
                    isone[i][j] = self.isonedigit(beginWord, wordList[j - 1])
                else:
                    isone[i][j] = self.isonedigit(wordList[i - 1], wordList[j - 1])
                isone[j][i] = isone[i][j]
        result = []
        result.append(beginWord)
        self.dfs(isone, wordList, used, endWord, 0, result)
        if len(self.results) == 0:
            return 0
        else:
            return min(map(len, self.results))
    
    def dfs(self, isone, wordList, used, endWord, index, result):
        if index > 0 and wordList[index - 1] == endWord:
            self.results.append(result.copy())
            return
        if sum(used) == len(wordList) + 1:
            return
        
        for i in range(1, len(wordList) + 1):
            if used[i] == 0 and isone[index][i] == 1:
                used[i] = 1
                result.append(wordList[i - 1])
                self.dfs(isone, wordList, used, endWord,i, result)
                used[i] = 0
                result.pop()
        return
        
    def isonedigit(self, s, t):
        for i in range(len(s)):
            if s[i] == t[i]:
                i += 1
            else:
                if s[i + 1:] == t[i + 1:]:
                    return 1
                else:
                    return 0
        return 0
    
import collections
from collections import deque
class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)   #to create a dictionary with empty list 
        wordList.append(beginWord)
        #adjacency list with pattern eg, hit: *it, h*t, hi* 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        
        res = 1     #since begin word is starting point so 1 length is starting
        q = deque([beginWord])
        visit = set([beginWord]) 

        #bfs 
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*"+ word[j+1:]  #generating patterns as above
                    for nbr in nei[pattern]:
                        if nbr not in visit:
                            visit.add(nbr)
                            q.append(nbr)
            res+=1
        return 0  #if we did not find any sequence
    
solution = Solution1()
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(solution.ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.ladderLength(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(solution.ladderLength(beginWord, endWord, wordList))