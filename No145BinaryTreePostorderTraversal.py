class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    nums = []
    def postorderTraversal(self, root):
        self.nums = []
        self.postorder(root)
        return self.nums
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        self.nums.append(node.val)
        

solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(solution.postorderTraversal(root))