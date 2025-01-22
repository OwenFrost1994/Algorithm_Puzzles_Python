# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            nonlocal result
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)
            return 1 + max(left, right)
        result = 0
        dfs(root)
        return result

solution = Solution()
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2), None)))
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))