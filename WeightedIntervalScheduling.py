def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        interval = []
        for _ in range(n):
            interval.append(list(map(int, input().split())))
        results.append(wis(interval))
    for result in results:
        print(result)

def wis(interval):
    n = len(interval)
    interval.sort(key=lambda x: x[1])
    p = c_p(interval, n)
    dp = [0] * n
    dp[0] = interval[0][2]
    for j in range(1, n):
        w = interval[j][2]
        if p[j] != -1:
            w += dp[p[j]]
        dp[j] = max(dp[j - 1], w)
    
    return max(dp)

def c_p(interval, n):
    p = [-1] * n
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            if interval[i][1] <= interval[j][0]:
                p[j] = i
                break
    return p

if __name__ == "__main__":
    main()