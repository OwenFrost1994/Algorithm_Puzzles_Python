class Solution:
    def numDistinct(self, s, t):
        if len(s) == len(t):
            if s == t:
                return 1
            else:
                return 0
            
        if len(s) < len(t):
            return 0
         
        dp = [[0]*len(t) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        k = 0
                        while k < i:
                            dp[i][j] = dp[i][j] + dp[k][j-1]
                            k = k + 1
        totoal = 0
        for i in range(len(s)):
            totoal = totoal + dp[i][len(t)-1]
        return totoal
    
class Solution1:
    def numDistinct(self, s, t):
        if len(s) == len(t):
            if s == t:
                return 1
            else:
                return 0
            
        if len(s) < len(t):
            return 0
        
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    if s[i-1] == t[j-1]:
                        if j == 0:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]
    
solution = Solution1()

s = "rabbbit"
t = "rabbit"
print(solution.numDistinct(s, t))

s = "babgbag"
t = "bag"
print(solution.numDistinct(s, t))