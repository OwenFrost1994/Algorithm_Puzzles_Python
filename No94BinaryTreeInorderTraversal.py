class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    nums = []
    def inorderTraversal(self, root):
        self.nums = []
        self.inorder(root)
        return self.nums
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.nums.append(node.val)
        self.inorder(node.right)

solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(solution.inorderTraversal(root))
