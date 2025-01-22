class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    nums = []
    def preorderTraversal(self, root):
        self.nums = []
        self.preorder(root)
        return self.nums
    def preorder(self, node):
        if node == None:
            return
        self.nums.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(solution.preorderTraversal(root))
