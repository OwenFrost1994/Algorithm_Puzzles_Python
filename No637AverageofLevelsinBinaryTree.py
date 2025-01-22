class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        result = []
        if root == None:
            return result
        parent = []
        child = []
        parent.append(root)

        while len(parent) > 0:
            sums = 0
            for i in range(len(parent)):
                sums += parent[i].val
                if parent[i].left != None:
                    child.append(parent[i].left)
                if parent[i].right != None:
                    child.append(parent[i].right)
            
            result.append(sums / len(parent))
            parent = child.copy()
            child = []
        return result
    
solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.averageOfLevels(root))