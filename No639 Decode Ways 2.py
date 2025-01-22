# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == '0':
#             return 0
#         n = len(s)
#         dp = [0]*(n + 1)
#         if s[0] == "*":
#             dp[0] = 9
#         else:
#             dp[0] = 1
#         for i in range(1, n + 1):
#             if s[i - 1] != '0':
#                 if i < n and s[i] == "*":
#                     dp[i] = 9*dp[i - 1]
#                 else:
#                     dp[i] = dp[i - 1]
#             if i >= 2:
#                 if s[i - 2] == "*" and s[i - 1] == "*":
#                      dp[i] = dp[i] + 15
#                 if s[i - 2] != "*" and s[i - 1] == "*":
#                     if int(s[i - 2]) < 2:
#                         dp[i] = dp[i] + 9
#                     if int(s[i - 2]) == 2:
#                         dp[i] = dp[i] + 6
#                 if s[i - 2] == "*" and s[i - 1] != "*":
#                     if int(s[i - 1]) <= 6:
#                         dp[i] = dp[i] + 2
#                     else:
#                         dp[i] = dp[i] + dp[i - 2]
#                 if s[i - 2] != "*" and s[i - 1] != "*":
#                     if 10 <= int(s[i - 2: i]) <= 26:
#                         dp[i] += dp[i - 2]
#         return dp[n]

from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(1,27): d[str(i)] = 1
        for i in range(10): d["*"+str(i)] = 1 + (i< 7)
        d['*'], d['**'], d['1*'], d['2*']  = 9,15,9,6

        n, M = len(s)-1, 10**9+7
        dp = [d[s[0]]] + [0]*n + [1]

        for i in range(n):
            one, two = s[i+1], s[i]+s[i+1]

            dp[i+1] = (d[one] * dp[i  ] + 
                       d[two] * dp[i-1])%M
            if not dp[i+1]: return 0
            
        return dp[-2]

solution = Solution()

s = "*"
print(solution.numDecodings(s))

s = "1*"
print(solution.numDecodings(s))

s = "2*"
print(solution.numDecodings(s))

s = "**"
print(solution.numDecodings(s))