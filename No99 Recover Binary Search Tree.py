class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

solution = Solution()
root = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
print(solution.recoverTree(root))

root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2), None))
print(solution.recoverTree(root))