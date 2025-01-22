class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.maxLen = 0
        def dfs(root: TreeNode, lastVal: int, curLen: int) -> None:
            if not root:
                return
            if lastVal != None and root.val == lastVal + 1:
                curLen += 1
            else:
                curLen = 1
            self.maxLen = max(self.maxLen, curLen)
            dfs(root.left, root.val, curLen)
            dfs(root.right, root.val, curLen)
            return
        
        dfs(root, None, 0)
        return self.maxLen
    
solution = Solution()
root = TreeNode(1, None, TreeNode(3, TreeNode(2), TreeNode(4, TreeNode(5))))
print(solution.longestConsecutive(root))
root = TreeNode(2, None, TreeNode(3, TreeNode(2, TreeNode(1), None), None))
print(solution.longestConsecutive(root))