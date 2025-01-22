class Solution:
    def findMinHeightTrees(self, n: int, edges):
        if n == 1:
            return [0]
        
        adj = [[] for x in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                # If the neighbor becomes a new leaf node, add it to the list
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        return leaves
    
solution = Solution()

n = 4
edges = [[1,0],[1,2],[1,3]]
print(solution.findMinHeightTrees(n, edges))

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(solution.findMinHeightTrees(n, edges))