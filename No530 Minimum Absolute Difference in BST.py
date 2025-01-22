# 这里没有注意到BST的属性是顺序排序，需要知道prev的值然后算差值，需要中序便利
# Definition for a binary tree node.
from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return
            nonlocal result, prev
            dfs(root.left)
            result = min(result, abs(prev - root.val))
            prev = root.val
            dfs(root.right)
        result = prev = inf
        dfs(root)
        return result

solution = Solution()
print(solution.getMinimumDifference(root = TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, 911))))
print(solution.getMinimumDifference(root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
print(solution.getMinimumDifference(root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))))