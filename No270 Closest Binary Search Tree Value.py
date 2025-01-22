class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
  def closestValue(self, p, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    result = p.val
    while p:
        if abs(target - p.val) < abs(result - target):
            result = p.val
        if target < p.val:
            p = p.left
        else:
            p = p.right
    return result
class Solution:
    def closestValue(self, root, target: float) -> int:
        
        self.diff = abs(root.val - target)
        self.val = root.val
        def dfs(root, target):
            if not root:
                return

            if self.diff >= abs(root.val - target):
                if self.diff == abs(root.val - target):
                    self.val = min(self.val, root.val)
                else:
                    self.val = root.val
                self.diff = abs(root.val - target)

            if root.val > target:
                dfs(root.left, target)
            
            if root.val < target:
                dfs(root.right, target)
            
        dfs(root, target)
        return self.val
solution = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(solution.closestValue(root, 3.5))

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(solution.closestValue(root, 4.5))

root = TreeNode(4, TreeNode(5, TreeNode(1), TreeNode(3)), TreeNode(5))
print(solution.closestValue(root, 3.714286))

root = TreeNode(1, TreeNode(2), TreeNode(5))
print(solution.closestValue(root, 4.428571))

root = TreeNode(1)
print(solution.closestValue(root, 4.428571))