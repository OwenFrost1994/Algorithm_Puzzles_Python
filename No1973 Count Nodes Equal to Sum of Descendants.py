# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return 0
            nonlocal result
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)
            rootsum = leftsum + rightsum
            if root.val == rootsum:
                result += 1
            return rootsum + root.val
        
        result = 0
        dfs(root)
        return result

solution = Solution()
print(solution.equalToDescendants(TreeNode(10, TreeNode(3, TreeNode(2), TreeNode(1)), TreeNode(4))))
print(solution.equalToDescendants(TreeNode(2, TreeNode(3, TreeNode(2), None), None)))