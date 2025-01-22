class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p != None and q != None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    
solution = Solution()

root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.isSameTree(root1, root2))

root1 = TreeNode(1, TreeNode(2), None)
root2 = TreeNode(1, None, TreeNode(2))
print(solution.isSameTree(root1, root2))

root1 = TreeNode(1, TreeNode(2), TreeNode(1))
root2 = TreeNode(1, TreeNode(1), TreeNode(2))
print(solution.isSameTree(root1, root2))