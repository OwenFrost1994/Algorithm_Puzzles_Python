from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        leaves = {}
        def dfs(root):
            if root.left == None and root.right == None:
                if 1 not in leaves.keys():
                    leaves[1] = []
                leaves[1].append(root.val)
                return 1
            l, r = 0, 0
            if root.left:
                l = dfs(root.left)
            if root.right:
                r = dfs(root.right)
            level = max(l, r) + 1
            if level not in leaves.keys():
                leaves[level] = []
            leaves[level].append(root.val)
            return level
        dfs(root)
        n = len(leaves)
        results = []
        for i in range(n):
            result = leaves[i + 1]
            results.append(result.copy())
        return results

solution = Solution()
root = TreeNode(1)
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2))
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, None, TreeNode(7))), TreeNode(3, None, TreeNode(6)))
print(solution.findLeaves(root))
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), None)), TreeNode(3, None, TreeNode(6)))
print(solution.findLeaves(root))
