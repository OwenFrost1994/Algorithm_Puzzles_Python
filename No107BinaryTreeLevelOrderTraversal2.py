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
        child = []
        parent.append(root)
        while len(parent) > 0:
            for i in range(len(parent)):
                if parent[i].left != None:
                    child.append(parent[i].left)
                if parent[i].right != None:
                    child.append(parent[i].right)
            result.append(parent.copy())
            parent = child.copy()
            child = []
            
        val = []
        while len(result) > 0:
            parentvalue = []
            parent = result.pop()
            for i in range(len(parent)):
                parentvalue.append(parent[i].val)
            val.append(parentvalue.copy())
        return val

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.levelOrder(root))