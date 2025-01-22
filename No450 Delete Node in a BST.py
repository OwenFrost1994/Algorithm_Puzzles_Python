# 二分搜索树的增删改查，这里面问题在于如果右或者左子树两个分支都满了怎么办，root的左/右树，就要挂到最底层节点上
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        node = root.right
        while node.left:
            node = node.left
        node.left = root.left
        root = root.right
        return root

solution = Solution()
print(solution.deleteNode(root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), key = 3))
print(solution.deleteNode(root = TreeNode(5, TreeNode(2, None, TreeNode(4)), TreeNode(6, None, TreeNode(7))), key = 0))
print(solution.deleteNode(root = None, key = 0))