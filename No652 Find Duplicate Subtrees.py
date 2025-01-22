# 我一开始的想法是用一个list存所有的子树头节点，便利过程中每出现一个子树都跟已经存进去的比，这样看着效率还行但是内存占的大
# 高手的办法是搞了一个dict计数并且把子树转为str再作为key來计数

# Definition for a binary tree node.
from collections import Counter
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            if not root:
                return "#"
            trees = str(root.val) + "," + dfs(root.left) + "," + dfs(root.right)
            c[trees] += 1
            if c[trees] == 2:
                result.append(root)
            return trees
        result = []
        c = Counter()
        dfs(root)
        return result

solution = Solution()
result = solution.findDuplicateSubtrees(root = TreeNode(2, TreeNode(1), TreeNode(1)))
result = solution.findDuplicateSubtrees(root = TreeNode(2, TreeNode(2, TreeNode(3), None), TreeNode(2, TreeNode(3),None)))
result = solution.findDuplicateSubtrees(root = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))))
    