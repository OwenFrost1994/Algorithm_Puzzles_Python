from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        return
    
solution = Solution()
root = solution.printTree(root = TreeNode(1, TreeNode(2), None))
root = solution.printTree(root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)))
