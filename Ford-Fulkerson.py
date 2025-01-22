from collections import defaultdict, deque


def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, m = map(int, input().split()) # n = |V|, m = |E|
        graph = defaultdict(lambda: defaultdict(int))
        for _ in range(m):
            u, v, c = list(map(int, input().split()))
            graph[u][v] += c
        results.append(FF(graph, 1, n))
    for result in results:
        print(result)

def FF(graph, src, dst):
    p = {}
    max_val = 0
    
    while bfs(graph, src, dst, p):
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

def bfs(graph, src, dst, p):
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