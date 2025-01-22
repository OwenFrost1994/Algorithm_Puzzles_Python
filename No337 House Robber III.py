class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# every node has two status: robbed and skipped, if this node is robbed, its child nodes must be skipped
# if this node is skipped, its child nodes can be skipped or robbed
class Solution:
    def rob(self, root) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            left = dfs(root.left) # contians if the maximum amount left is robbed or skipped
            right = dfs(root.right) # contians if the maximum amount right is robbed or skipped
            rob = root.val + left[1] + right[1] # if this node is robbed, left and right must be skipped
            skip = max(left) + max(right) # if this node is skipped, left and right can be either skipped or robbed
            return rob, skip
        return max(dfs(root))

solution = Solution()
root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
print(solution.rob(root))
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
print(solution.rob(root))