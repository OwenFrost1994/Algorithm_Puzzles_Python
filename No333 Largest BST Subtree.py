from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root) -> int:
        def dfs(root):
            if not root:
                return inf, -inf, 0
            lmin, lmax, ln = dfs(root.left)
            rmin, rmax, rn = dfs(root.right)

            if root.val > lmax and root.val < rmin:
                self.result = max(self.result, ln + rn + 1)
                return min(lmin, root.val), max(rmax, root.val), ln + rn + 1
            return -inf, inf, 0
        
        self.result = 0
        dfs(root)
        return self.result

solution = Solution()
root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, None, TreeNode(7))) # [10,5,15,1,8,null,7]
print(solution.largestBSTSubtree(root))
