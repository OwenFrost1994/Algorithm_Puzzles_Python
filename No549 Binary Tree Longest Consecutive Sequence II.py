# 这个问题需要返回左侧节点的值和右侧节点的值
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                # val, increasing length, decreasing length, max length
                return float('-inf'), 0, 0, 0
            # inc/dec starting from root
            inc = dec = 1
            left, leftInc, leftDec, leftMax = dfs(root.left) # grab the length 
            right, rightInc, rightDec, rightMax = dfs(root.right) # grab the right
            if root.val + 1 == left:
                inc = max(leftInc + 1, inc) #cannot just add one since the increasing is not fixed from left or right
            if root.val - 1 == left:
                dec = max(leftDec+ 1, dec)
            if root.val + 1 == right:
                inc = max(rightInc + 1, inc)
            if root.val - 1 == right:
                dec = max(rightDec + 1, dec)
            return root.val, inc, dec, max(inc + dec - 1, leftMax, rightMax, inc, dec)
        return dfs(root)[3]


solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.longestConsecutive(root))
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution.longestConsecutive(root))