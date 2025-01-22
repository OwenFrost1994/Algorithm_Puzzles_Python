# 这个拆分字符串太恶心了
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def dfs(s):
            if not s:
                return None
            lp = s.find("(")
            if lp == -1:
                return TreeNode(int(s))
            root = TreeNode(int(s[:lp]))
            cnt = 0
            start = lp
            for i in range(lp, len(s)):
                if s[i] == "(":
                    cnt += 1
                if s[i] == ")":
                    cnt -= 1
                if cnt == 0:
                    if start == lp:
                        root.left = dfs(s[start + 1:i])
                        start = i + 1
                    else:
                        root.right = dfs(s[start + 1:i])
            return root
        return dfs(s)
    
solution = Solution()
result = solution.str2tree(s = "4(2()(1))(6(5))")
result = solution.str2tree(s = "4(2(3)(1))(6(5))")
result = solution.str2tree(s = "4(2(3)(1))(6(5)(7))")
result = solution.str2tree(s = "-4(2(3)(1))(6(5)(7))")