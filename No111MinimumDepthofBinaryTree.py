class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if root.left and root.right:
            return min(left, right) + 1
        
        return max(left, right) + 1

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.minDepth(root))

root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(solution.minDepth(root))