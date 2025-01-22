class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    preindex = 0
    def buildTree(self, preorder, inorder):
        return self.addtreenode(0, len(inorder)-1, preorder, inorder)
    def addtreenode(self, left, right, preorder, inorder):
        if left > right:
            return None
        treenode = TreeNode(preorder[self.preindex])
        self.preindex += 1

        mid = 0
        for i in range(left, right + 1):
            if inorder[i] == treenode.val:
                mid = i
                break
        
        treenode.left = self.addtreenode(left, mid - 1, preorder, inorder)
        treenode.right = self.addtreenode(mid + 1, right, preorder, inorder)

        return treenode

solution = Solution()

preorder = [3,9,20,15,7] #the node vale is added first
inorder = [9,3,15,20,7] #the node value is added after the left
print(solution.buildTree(preorder, inorder))
