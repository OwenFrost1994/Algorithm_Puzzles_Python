class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur = root
        ans = None

        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                ans = cur
                cur = cur.left
        return ans

solution = Solution()
p = TreeNode(1)
root = TreeNode(2, p, TreeNode(3))
successor = solution.inorderSuccessor(root, p)
p = TreeNode(6)
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), p)
successor = solution.inorderSuccessor(root, p)