# 这个要求找到leaf，高手的代码简洁的可怕，利用了py的list求和功能
# https://leetcode.com/problems/leaf-similar-trees/solutions/2889774/python-3-5-lines-recursion-w-example-t-m-95-88/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)
    
solution = Solution()
print(solution.leafSimilar(
    root1 = TreeNode(1, TreeNode(2), TreeNode(3)),
    root2=TreeNode(1, TreeNode(3), TreeNode(2))))
print(solution.leafSimilar(
    root1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8))), 
    root2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))))