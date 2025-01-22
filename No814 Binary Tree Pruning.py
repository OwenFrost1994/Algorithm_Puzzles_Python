# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root.left == None and root.right == None:
                if root.val == 0:
                    return True
                else:
                    return False
            if root.left != None:
                leftis = dfs(root.left)
            else:
                leftis = True
            if root.right != None:
                rightis = dfs(root.right)
            else:
                rightis = True
            if leftis:
                root.left = None
            if rightis:
                root.right = None
            return leftis and rightis and root.val == 0
        if root == None:
            return root
        iszero = dfs(root)
        return None if iszero else root

solution = Solution()
nroot = solution.pruneTree(root = TreeNode(1, TreeNode(1), TreeNode(0)))
nroot = solution.pruneTree(root = TreeNode(1, TreeNode(0), TreeNode(0)))
nroot = solution.pruneTree(root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1))))
nroot = solution.pruneTree(root = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1))))
nroot = solution.pruneTree(root = TreeNode(1, TreeNode(1, TreeNode(1, TreeNode(0), None), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1))))