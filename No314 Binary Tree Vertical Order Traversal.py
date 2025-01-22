from ast import List
from typing import Optional
from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]):
        column = defaultdict(list)
        nodes = deque()
        nodes.append((root, 0))
        while nodes:
            node, offset = nodes.popleft()
            column[offset].append(node.val)
            if node.left:
                nodes.append((node.left, offset - 1))
            if node.right:
                nodes.append((node.right, offset + 1))
        column = sorted(column.items())
        return [v for _, v in column]
    
solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.verticalOrder(root))

root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)), TreeNode(8, TreeNode(1), TreeNode(7)))
print(solution.verticalOrder(root))

root = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, TreeNode(5), None)), TreeNode(8, TreeNode(1, None, TreeNode(2)), TreeNode(7)))
print(solution.verticalOrder(root))
