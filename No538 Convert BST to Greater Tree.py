# 后序遍历且需要prev来记录和

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            nonlocal prev
            dfs(root.right)
            root.val += prev
            prev = root.val
            dfs(root.left)
        prev = 0
        dfs(root)
        return root

solution = Solution()
print(solution.convertBST(TreeNode(0, None, TreeNode(1))))
print(solution.convertBST(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))))
