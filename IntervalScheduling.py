def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        intervals = []
        for _ in range(n):
            intervals.append(list(map(int, input().split())))
        results.append(schedule(intervals))
    for result in results:
        print(result)

def schedule(intervals):
    intervals.sort(key = lambda x: (x[1], x[0]))
    end = 0
    n = 0
    for a, b in intervals:
        if a >= end:
            end = b
            n += 1
    return n

if __name__ == "__main__":
    main()