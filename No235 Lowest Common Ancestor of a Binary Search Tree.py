class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q or not root:
            return root
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)

        if l and r:
            return root
        elif l:
            return l
        elif r:
            return r

solution = Solution()
p = TreeNode(2)
p.left = TreeNode(0)
p.right = TreeNode(4)
p.right.left = TreeNode(3)
p.right.right = TreeNode(5)
q = TreeNode(8)
q.left = TreeNode(7)
q.right = TreeNode(9)
root = TreeNode(6)
root.left = p
root.right = q
print(solution.lowestCommonAncestor(root, p, q))

q = TreeNode(4)
q.left = TreeNode(3)
q.right = TreeNode(5)
p = TreeNode(2)
p.left = TreeNode(0)
p.right = q
root = TreeNode(6)
root.left = p
root.right =  TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
print(solution.lowestCommonAncestor(root, p, q))