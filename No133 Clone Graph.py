class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return None
        visited = {}
        nodes = deque()
        nodes.append(node)

        # initial node
        head = Node()
        head.val = node.val

        visited[node] = head
        while len(nodes) > 0:
            point = nodes.popleft()
            for neighbor in point.neighbors:
                if neighbor not in visited:
                    q = Node()
                    q.val = neighbor.val
                    visited[neighbor] = q
                    nodes.append(neighbor)
                visited[point].neighbors.append(visited[neighbor])
        return visited[node]


solution = Solution()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node3, node1]

print(solution.cloneGraph(node1))