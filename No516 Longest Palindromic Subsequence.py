# 这个要快必须用dp，dp[i][j]表示ij之间最长的回文，如果s[i] == s[j]，dp[i][j] = dp[i + 1][j - 1] + 2， 因为在i + 1, j - 1基础上加了2
# 如果 s[i] != s[j] ,那就看dp[i][j - 1] 或者 dp[i + 1][j]谁更大
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]

solution = Solution()
print(solution.longestPalindromeSubseq(s = "bbbab"))
print(solution.longestPalindromeSubseq(s = "cbbd"))