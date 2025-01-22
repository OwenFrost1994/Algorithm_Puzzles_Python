class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if root == None:
            return False
        return self.seachpath(root, 0, targetSum)
    
    def seachpath(self, root, sum, targetSum):
        # if sum == targetSum:
        #     return True 
        # if sum > targetSum:
        #     return False
        
        if root.left == None and root.right == None:
            return sum + root.val == targetSum
        else:
            if root.left != None:
                left = self.seachpath(root.left, sum + root.val, targetSum)
            else:
                left = False
            if root.right != None:
                right = self.seachpath(root.right, sum + root.val, targetSum)
            else:
                right = False
            return left or right

solution = Solution()
head = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(8, TreeNode(13), None), TreeNode(4, None, TreeNode(1))))
print(solution.hasPathSum(head, 22))

head = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.hasPathSum(head, 5))

head = None
print(solution.hasPathSum(head, 0))

head = TreeNode(1, TreeNode(2))
print(solution.hasPathSum(head, 0))