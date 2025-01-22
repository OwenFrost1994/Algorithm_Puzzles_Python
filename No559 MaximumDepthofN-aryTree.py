class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children    

class Solution:
    nums = []
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.children != None and len(root.children) > 0:
            depth = []
            for i in range(len(root.children)):
                depth.append(self.maxDepth(root.children[i]))
            return max(depth) + 1
        return 1

solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(solution.maxDepth(root))

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
print(solution.maxDepth(root))