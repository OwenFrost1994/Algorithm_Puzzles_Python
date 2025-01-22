def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, c = map(int, input().split())
        items = []
        for _ in range(n):
            items.append(list(map(int, input().split())))
        results.append(knapsack(items, c))
    for result in results:
        print(result)

def knapsack(items, c):
    if c == 0:
        return 0
    n = len(items)
    dp = [[0]*(c + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j >= items[i-1][0]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

if __name__ == "__main__":
    main()