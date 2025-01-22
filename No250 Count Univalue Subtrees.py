class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def recursion(root):
            if root == None:
                return True
            lefttrue = recursion(root.left)
            righttrue = recursion(root.right)
            if lefttrue and righttrue:
                if root.left and root.left.val != root.val:
                    return False
                if root.right and root.right.val != root.val:
                    return False
                self.count += 1
                return True
            return False
        self.count = 0
        recursion(root)
        return self.count

solution = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(5))
print(solution.countUnivalSubtrees(root))

root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
print(solution.countUnivalSubtrees(root))

print(solution.countUnivalSubtrees(None))

root = TreeNode(5, TreeNode(5, TreeNode(5), TreeNode(5)), TreeNode(5, None, TreeNode(5)))
print(solution.countUnivalSubtrees(root))