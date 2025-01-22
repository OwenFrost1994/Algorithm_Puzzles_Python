# level order transversal
# 这个是给BST编号的技巧
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        maxlen = 0
        while q:
            maxlen = max(maxlen, q[-1][1] - q[0][1] + 1)
            for i in range(len(q)):
                node, l = q.popleft()
                if node.left:
                    q.append((node.left, 2 * l))
                if node.right:
                    q.append((node.right, 2 * l + 1))    
        return maxlen

    
solution = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2))
print(solution.widthOfBinaryTree(root))
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
print(solution.widthOfBinaryTree(root))
root = TreeNode(1, TreeNode(3, TreeNode(5, TreeNode(6), None), None), TreeNode(2, None, TreeNode(9, TreeNode(7), None)))
print(solution.widthOfBinaryTree(root))