# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left, leftsum = dfs(root.left)
            right, rightsum = dfs(root.right)
            return abs(leftsum - rightsum), leftsum + rightsum + root.val
        return dfs(root)[0]