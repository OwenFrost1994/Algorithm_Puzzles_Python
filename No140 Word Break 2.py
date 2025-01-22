class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}
        wordSet = set(wordDict)
        result = []
        self.dfs(result, "", s, wordSet, memo)
        return result
    
    def dfs(self, result, news, s, wordSet, memo):
        # if s in wordSet:
        #     if news == "":
        #         result.append(news + s)
        #     else:
        #         result.append(news + " " + s)
        #     return True
        if s == "":
            result.append(news)
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if news == "":
                newss = news + prefix
            else:
                newss = news + " " + prefix
            if prefix in wordSet and self.dfs(result, newss, s[i:], wordSet, memo):
                memo[s] = True
        memo[s] = False
        return False

solution = Solution()
answer = ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(solution.wordBreak(s, wordDict))

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
print(solution.wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(solution.wordBreak(s, wordDict))

s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]
print(solution.wordBreak(s, wordDict))
