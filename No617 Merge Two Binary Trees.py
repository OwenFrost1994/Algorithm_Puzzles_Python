from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 == None and node2 == None:
                return
            if node1 != None:
                if node2 != None:
                    node1.val = node1.val + node2.val
                    node1.left = dfs(node1.left, node2.left)
                    node1.right = dfs(node1.right, node2.right)
            else:
                node1 = node2
            return node1
        return dfs(root1, root2)

solution = Solution()
root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
root = solution.mergeTrees(root1, root2)

root1 = TreeNode(1)
root2 = TreeNode(1, TreeNode(2))
root = solution.mergeTrees(root1, root2)