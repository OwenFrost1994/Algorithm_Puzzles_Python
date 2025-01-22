class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]

class Solution1:
    def wordBreak(self, s, wordDict):
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)
    
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if s in wordSet:
            return True
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix in wordSet and self.dfs(s[i:], wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False

solution = Solution1()

s = "leetcode"
wordDict = ["leet","code"]
print(solution.wordBreak(s, wordDict))

s = "applepenapple"
wordDict = ["apple","pen"]
print(solution.wordBreak(s, wordDict))

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(solution.wordBreak(s, wordDict))