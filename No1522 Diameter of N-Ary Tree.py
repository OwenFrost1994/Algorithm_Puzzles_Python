# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        def dfs(root):
            if not root.children:
                return 1
            nonlocal result
            dis = []
            for children in root.children: 
                dis.append(dfs(children))
            dis.sort()
            mx = dis[-1]
            if len(dis) > 1:
                mx += dis[-2]
            result = max(result, mx)
            return 1 + max(dis)
        result = 0
        dfs(root)
        return result
solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(solution.diameter(root))

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
print(solution.diameter(root))