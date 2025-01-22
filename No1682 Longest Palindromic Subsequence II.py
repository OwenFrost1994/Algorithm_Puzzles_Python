class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[[0] * 26 for _ in range(length)] for _ in range(length)]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1,length):
                for k in range(26):
                    c = chr(ord('a') + k)
                    if s[i] != c:
                        dp[i][j][k] = dp[i + 1][j][k]
                    elif s[j] != c:
                        dp[i][j][k] = dp[i][j - 1][k]
                    else:
                        prevLength = max(dp[i + 1][j - 1][m] for m in range(26) if m != k)
                        dp[i][j][k] = prevLength + 2
        maxLength = 0
        for k in range(26):
            maxLength = max(maxLength, dp[0][length - 1][k])
        return maxLength
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         @cache
#         def dfs(i, j, x):
#             if i >= j: # i==j, then it's an odd one, not valid
#                 return 0
#             if s[i] == s[j] and s[i] != x:
#                 return dfs(i + 1, j - 1, s[i]) + 2
#             return max(dfs(i + 1, j, x), dfs(i, j - 1, x))

#         ans = dfs(0, len(s) - 1, '')
#         dfs.cache_clear()
#         return ans
    
solution = Solution()
print(solution.longestPalindromeSubseq(s = "bbabab"))
print(solution.longestPalindromeSubseq(s = "dcbccacdb"))