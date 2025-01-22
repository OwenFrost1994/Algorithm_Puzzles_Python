# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ""
            trees = str(root.val) 
            if root.left != None or root.right != None:
                trees += "(" + str(dfs(root.left)) + ")"
            if root.right != None:
                trees += "(" + str(dfs(root.right)) + ")"
            return trees
        return dfs(root)

solution = Solution()
result = solution.tree2str(root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3)))
result = solution.tree2str(root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)))