class Solution:
    def validTree(self, n: int, edges) -> bool:
        connect = {}
        nodes = [0]*n
        nedges = len(edges)
        for i in range(n):
            connect[i] = []
        for i in range(nedges):
            connect[edges[i][0]].append(edges[i][1])
            connect[edges[i][1]].append(edges[i][0])
            nodes[edges[i][0]] += 1
            nodes[edges[i][1]] += 1
        if len(connect) < n:
            return False
        leaf = []
        for i in range(n):
            if nodes[i] == 1:
                leaf.append(i)
        while leaf:
            node = leaf.pop(0)
            nodes[node] = 0
            for onodes in connect[node]:
                connect[onodes].remove(node)
                nodes[onodes] -= 1
                if nodes[onodes] == 1:
                    leaf.append(onodes)
            connect.pop(node)
        return sum(nodes) == 0

solution = Solution()
print(solution.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
print(solution.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))