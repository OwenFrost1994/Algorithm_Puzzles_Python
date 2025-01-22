from collections import defaultdict
from math import inf

def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        m = int(input().strip())
        requests = list(map(int, input().split()))
        results.append(FF(n, requests))
    for result in results:
        print(result)

def FF(n, q):
    faults = 0
    cache = set()
    mp = defaultdict(list)
    for i, v in enumerate(q):
        mp[v].append(i)
    for i in range(len(q)):
        if q[i] not in cache:
            faults += 1
            if len(cache) == n:
                fpage = 0
                fdist = 0
                for p in cache:
                    if len(mp[p]) == 0:
                        dist = inf
                    else:
                        dist = mp[p][0]
                    if dist > fdist:
                        fpage = p
                        fdist = dist
                cache.remove(fpage)
        cache.add(q[i])
        mp[q[i]].pop(0)
    return faults

if __name__ == "__main__":
    main()