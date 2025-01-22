class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root):
        if root == None:
            return []
        result = []
        nodes = deque()
        nodes.append(root)
        while nodes:
            result.append(nodes[-1].val)
            leng = len(nodes)
            for i in range(leng):
                node = nodes.popleft()
                if node.left != None:
                    nodes.append(node.left)
                if node.right != None:
                    nodes.append(node.right)
        return result

solution = Solution()

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(solution.rightSideView(root))

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(solution.rightSideView(root))