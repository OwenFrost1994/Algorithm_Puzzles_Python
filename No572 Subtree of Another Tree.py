# 这个比较的时候要从根节点开始，recursion比较左右节点是不是一样
# 直到所有下面的子节点都是none才返回true，想通了这一点就比较好写
# false条件就是二者其中一个是none或者值不一样
# https://leetcode.com/problems/subtree-of-another-tree/solutions/4379727/bfs-python-o-n-m/

# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot or root.val != subRoot.val:
                return False
            return compare(root.left, subRoot.left) and compare(root.right, subRoot.right)
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    if compare(node, subRoot):
                        return True
                    queue.append(node.left)
                    queue.append(node.right)
        return False

solution = Solution()
print(solution.isSubtree(root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)), subRoot = TreeNode(4, TreeNode(1), TreeNode(2))))
print(solution.isSubtree(root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None)), TreeNode(5)), subRoot = TreeNode(4, TreeNode(1), TreeNode(2))))