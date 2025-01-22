class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    paths = []
    def pathSum(self, root, targetSum):
        self.paths = []
        self.seachpath(root, 0, [], targetSum)
        return self.paths
    
    def seachpath(self, root, sum, path, targetSum):
        if root == None:
            return
        if root.left == None and root.right == None:
            if sum + root.val == targetSum:
                path.append(root.val) 
                self.paths.append(path.copy())
            return 
        else:
            path.append(root.val) 
            if root.left != None:
                self.seachpath(root.left, sum + root.val, path.copy(), targetSum)
            if root.right != None:
                self.seachpath(root.right, sum + root.val, path.copy(), targetSum)
        path.pop()

solution = Solution()
head = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
print(solution.pathSum(head, 22))

head = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.pathSum(head, 5))

head = None
print(solution.pathSum(head, 0))

head = TreeNode(1, TreeNode(2))
print(solution.pathSum(head, 0))