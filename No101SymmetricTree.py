# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        return self.ismirror(root, root)
    
    def ismirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 != None and node2 != None:
            if node1.val == node2.val:
                return (self.ismirror(node1.left, node2.right) and self.ismirror(node1.right, node2.left))
        return False
    
solution = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(2, TreeNode(3), TreeNode(4)))
print(solution.isSymmetric(root))

root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(solution.isSymmetric(root))