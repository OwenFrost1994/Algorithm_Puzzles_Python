from collections import defaultdict, deque


def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, m, q = map(int, input().split()) # n = |A|, m = |B|, q = |E|
        graph = defaultdict(lambda: defaultdict(int))
        for _ in range(q):
            u, v = list(map(int, input().split()))
            graph[u][n + v] = 1
        for i in range(n): # from source to A set
            graph[0][i + 1] = 1
        for i in range(m): # from B set to sink
            graph[n + i + 1][n + m + 1] = 1
        maxflow = Match(graph, 0, n + m + 1)
        if maxflow == m and maxflow == n:
            results.append(str(maxflow) + " " + "Y")
        else:
            results.append(str(maxflow) + " " + "N")
    for result in results:
        print(result)

def Match(graph, src, dst):
    p = {}
    max_val = 0
    
    while dfs(graph, src, dst, p):
        path_flow = float('Inf')
        s = dst
        while s != src:
            path_flow = min(path_flow, graph[p[s]][s])
            s = p[s]
        v = dst
        while v != src:
            u = p[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = p[v]
        max_val += path_flow
    return max_val

def dfs(graph, src, dst, p):
    visited = set()
    queue = deque([src])
    visited.add(src)
    
    while queue:
        node = queue.popleft()
        for next, c in graph[node].items():
            if next not in visited and c > 0:
                p[next] = node
                if next == dst:
                    return True
                queue.append(next)
                visited.add(next)
    return False
    
if __name__ == "__main__":
    main()