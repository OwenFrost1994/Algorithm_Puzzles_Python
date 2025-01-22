class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        self.result = 0
        def dfs(root):
            if not root:
                return
            if root.left != None and root.left.left == None and root.left.right == None:
                self.result += root.left.val
            else:
                dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.result

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.sumOfLeftLeaves(root))