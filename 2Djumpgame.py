m = 7
n = 5
a = 1
b = 4
dp = [[0]*n for _ in range(m)]
for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - a][j] + dp[i][j - a] + dp[i - b][j] + dp[i][j - b]
print(dp[-1][-1])