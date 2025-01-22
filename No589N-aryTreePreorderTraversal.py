class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children    

class Solution:
    nums = []
    def preorder(self, root):
        self.nums = []
        self.pre(root)
        return self.nums
    
    def pre(self, node):
        if node == None:
            return
        self.nums.append(node.val)
        if node.children != None:
            for i in range(len(node.children)):
                self.pre(node.children[i])
        else:
            return

solution = Solution()
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(solution.preorder(root))

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
print(solution.preorder(root))