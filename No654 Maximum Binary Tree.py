# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recursion(nums):
            if len(nums) == 1:
                return TreeNode(nums[0])
            val = max(nums)
            idx = nums.index(val)
            left, right = None, None
            if idx != 0:
                left = recursion(nums[:idx])
            if idx != len(nums) - 1:
                right = recursion(nums[idx + 1:])
            return TreeNode(val, left, right)
        return recursion(nums)

solution = Solution()
root = solution.constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
from tools import printtree
printtree(root)
root = solution.constructMaximumBinaryTree(nums = [3,2,1])
printtree(root)