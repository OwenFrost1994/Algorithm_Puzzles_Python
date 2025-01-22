class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int):
        result = []

        def recursion(root):
            if root == None:
                return
            recursion(root.left)
            if len(result) < k:
                result.append(root.val)
            else:
                if abs(root.val - target) >= abs(result[0] - target):
                    return
                result.pop(0)
                result.append(root.val)
            recursion(root.right)
        
        recursion(root)
        return result

solution = Solution()

root = TreeNode(4, TreeNode(5, TreeNode(1), TreeNode(3)), TreeNode(5))
print(solution.closestKValues(root, 3.714286, 2))

root = TreeNode(1)
print(solution.closestKValues(root, 0.000000, 1))
