class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        if root == None:
            return root
        leftlist = None
        rightlist = None
        if root.left != None:
            leftlist = self.flatten(root.left)
        if root.right != None:
            rightlist = self.flatten(root.right)
        root.right = leftlist
        root.left = None

        point = root
        while point.right != None:
            point = point.right
        point.right = rightlist

        return root

solution = Solution()
head = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
print(solution.flatten(head))

head = None
print(solution.flatten(head))