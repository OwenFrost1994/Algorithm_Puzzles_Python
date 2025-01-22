def main():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        mp = {}
        for _ in range(n):
            line = input().split()
            mp[line[0]] = line[1:] 
        results.append(dfs(mp))

    for result in results:
        print(result)

def dfs(mp):
    result = []
    visited = set()
    def recursion(root):
        if root in visited:
            return
        result.append(root)
        visited.add(root)
        for node in mp[root]:
            recursion(node)
    for key in list(mp.keys()):
        if key not in visited:
            recursion(key)
    return " ".join(result)

if __name__ == "__main__":
    main()