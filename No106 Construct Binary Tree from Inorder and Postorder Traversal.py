class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    postindex = 0
    def buildTree(self, inorder, postorder):
        self.postindex = len(inorder) - 1
        return self.addtreenode(0, len(inorder) - 1, inorder, postorder)
    
    def addtreenode(self, left, right, inorder, postorder):
        if left > right:
            return None
        treenode = TreeNode(postorder[self.postindex])
        self.postindex -= 1

        mid = 0
        for i in range(left, right + 1):
            if inorder[i] == treenode.val:
                mid = i
                break
        
        treenode.right = self.addtreenode(mid + 1, right, inorder, postorder)
        treenode.left = self.addtreenode(left, mid - 1, inorder, postorder)

        return treenode

solution = Solution()

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(solution.buildTree(inorder, postorder))