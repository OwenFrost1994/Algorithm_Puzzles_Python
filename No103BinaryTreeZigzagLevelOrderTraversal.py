class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        result = []
        if root == None:
            return result
        parent = []
        parentvalue = []
        child = []
        parent.append(root)
        left = 1
        while len(parent) > 0:
            for i in range(len(parent)):
                if parent[i].left != None:
                    child.append(parent[i].left)
                if parent[i].right != None:
                    child.append(parent[i].right)
            if left == 1:
                for i in range(len(parent)):
                    parentvalue.append(parent[i].val)
                left = 0
            else:
                for i in range(len(parent)-1, -1, -1):
                    parentvalue.append(parent[i].val)
                left = 1
            parent = child.copy()
            child = []
            result.append(parentvalue.copy())
            parentvalue = []
        return result

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.levelOrder(root))