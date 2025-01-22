class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
  def upsideDownBinaryTree(self, root):
    if root == None:
       return root
    if root.left == None:
       return root
    newroot = self.upsideDownBinaryTree(root.left)
    if root.left != None:
       root.left.left = root.right
       root.left.right = root
       root.left = None
       root.right = None
    return newroot

solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
newroot = solution.upsideDownBinaryTree(root)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
newroot = solution.upsideDownBinaryTree(root)

newroot = solution.upsideDownBinaryTree(None)

root = [1]
newroot = solution.upsideDownBinaryTree(TreeNode(1))