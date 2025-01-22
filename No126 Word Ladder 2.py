class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        self.results = []
        if endWord not in wordList:
            return []
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
            return self.results
        else:
            final = []
            minlen = min(map(len, self.results))
            for i in range(len(self.results)):
                if len(self.results[i]) == minlen:
                    final.append(self.results[i].copy())
            return final
    
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

from collections import deque
class Solution1:
    def findLadders(self, beginWord, endWord, wordList):
        def dfs(word,a):
            if word==beginWord:
                ans.append(a[::-1])
                return
            n=d[word]-1
            for i in range(l):
                for j in range(26):
                    new=word[:i]+chr(97+j)+word[i+1:]
                    if new in d and d[new]==n:
                        a.append(new)
                        dfs(new,a)
                        a.pop()
            return ans
                 
        wordList=set(wordList)
        wordList.discard(beginWord)
        if endWord not in wordList:
            return []
        q=deque([beginWord])
        ans=[]
        d=dict()
        d[beginWord]=1
        level=1
        t=set()
        l=len(beginWord)
        while q:
            word=q.popleft()
            if word==endWord:
                break
            for i in range(l):
                for j in range(26):
                    new=word[:i]+chr(97+j)+word[i+1:]
                    if new in wordList:
                        d[new]=d[word]+1
                        q.append(new)
                        wordList.remove(new)         
        if endWord in d:
            dfs(endWord, [endWord])
        return ans
    
solution = Solution1()
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
print(solution.findLadders(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(solution.findLadders(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(solution.findLadders(beginWord, endWord, wordList))