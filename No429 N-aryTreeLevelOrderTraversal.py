class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        parent = []
        parentvalue = []
        child = []
        parent.append(root)
        while len(parent) > 0:
            for i in range(len(parent)):
                parentvalue.append(parent[i].val)
                if parent[i].children != None:
                    child = child + parent[i].children
            parent = child.copy()
            child = []
            result.append(parentvalue.copy())
            parentvalue = []

        return result
    
solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(solution.levelOrder(root))

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
print(solution.levelOrder(root))