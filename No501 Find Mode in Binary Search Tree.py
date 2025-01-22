# 这里注意遍历的时候，一个记录前一个节点值的变量prev和记录最大频率的变量maxf是不会被冲掉的，因为他每次就搜索一个点
# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal prev, maxf, result, c
            if root.val == prev:
                c += 1
            else:
                c = 1
            if c > maxf:
                result = [root.val]
                maxf = c
            elif c == maxf:
                result.append(root.val)
            prev = root.val
            dfs(root.right)
        result = []
        maxf = 0
        prev = None
        c = 0
        dfs(root)
        return  result
    
solution = Solution()
print(solution.findMode(TreeNode(0)))
print(solution.findMode(TreeNode(1, None, TreeNode(2, TreeNode(2, None)))))
