# 做了很多分层遍历的题，这种基本上就是deque
# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        left = 0
        while q:
            left = q[0].val
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return left
    
solution = Solution()
print(solution.findBottomLeftValue(TreeNode(2, TreeNode(1), TreeNode(3))))
print(solution.findBottomLeftValue(TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, TreeNode(5), TreeNode(6)))))