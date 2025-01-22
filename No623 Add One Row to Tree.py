# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val, root, None)
            return root
        def dfs(root, dep):
            if not root:
                return
            if dep == depth - 1:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
                return
            dfs(root.left, dep + 1)
            dfs(root.right, dep + 1)
        dfs(root, 1)
        return root

solution = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5), None))
root_new = solution.addOneRow(root, 1, 1)
root_new = solution.addOneRow(root, 1, 2)
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), None)
root_new = solution.addOneRow(root, 1, 3)
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), None)
root_new = solution.addOneRow(root, 5, 4)