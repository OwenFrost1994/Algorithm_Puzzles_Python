# 一个很典的 post-order transversal，肯定先检查节点的和再看加上根节点的和
# Definition for a binary tree node.
from collections import Counter
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if root == None:
                return 0
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)
            rootsum = leftsum + rightsum + root.val
            c[rootsum] += 1
            return rootsum
        
        c = Counter()
        dfs(root)
        maxf = max(c.values())
        return [k for k, v in c.items() if v == maxf]

solution = Solution()
print(solution.findFrequentTreeSum(TreeNode(5, TreeNode(2), TreeNode(-3))))