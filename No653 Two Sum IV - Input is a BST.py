class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k):
        def dfs(node, seen):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)            
            return dfs(node.left, seen) or dfs(node.right, seen)
        
        return dfs(root, set())

solution = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
k = 9
print(solution.findTarget(root, k))