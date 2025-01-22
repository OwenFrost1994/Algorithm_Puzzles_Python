class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from math import inf
from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        result = []
        while q:
            mx = -inf
            for i in range(len(q)):
                node = q.popleft()
                mx = max(mx, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(mx)
        return result