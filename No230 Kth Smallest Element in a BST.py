class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        num = []
        return self.preorder(root, num, k)
    def preorder(self, root, num, k):
        if root == None:
            return
        self.preorder(root.left, num, k)
        if len(num) < k:
            num.append(root.val)
        if len(num) < k:
            self.preorder(root.right, num, k)
        if len(num) >= k:
            return num[k - 1]


solution = Solution()
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
k = 1
print(solution.kthSmallest(root, k))

root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6))
k = 3
print(solution.kthSmallest(root, k))