class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if not root:
            return 0
        return self.maxDepth(root) != -1
    
    def maxDepth(self, root):
        if not root:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        if right == -1 or left == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.maxDepth(root))

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(solution.maxDepth(root))