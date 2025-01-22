class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def countNodes(self, root) -> int:
        if root == None:
            return 0
        nodes = deque()
        nodes.append(root)
        num = 0
        while nodes:
            num += len(nodes)
            n = len(nodes)
            for i in range(n):
                node = nodes.popleft()
                if node.left != None:
                    nodes.append(node.left)
                if node.right != None:
                    nodes.append(node.right)
            
        return num
    
solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
print(solution.countNodes(root))

solution = Solution()
print(solution.countNodes(None))