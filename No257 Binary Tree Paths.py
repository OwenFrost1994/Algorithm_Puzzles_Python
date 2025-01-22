class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    paths = []
    def binaryTreePaths(self, root):
        self.paths = []
        self.seachpath(root, "")
        return self.paths
    
    def seachpath(self, root, path):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.paths.append(path + str(root.val))
            return 
        else:
            if root.left != None:
                self.seachpath(root.left, path + str(root.val) + "->")
            if root.right != None:
                self.seachpath(root.right, path + str(root.val) + "->")

solution = Solution()
head = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(solution.binaryTreePaths(head))

head = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.binaryTreePaths(head))

head = None
print(solution.binaryTreePaths(head))

head = TreeNode(1)
print(solution.binaryTreePaths(head))