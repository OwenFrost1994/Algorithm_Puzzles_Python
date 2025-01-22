class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        stack=[]
        stack.append([root,-1*float('inf'),float('inf')])
        while(stack):
            s=stack.pop()
            t=s[0]
            le=s[1]
            ri=s[2]
            if t.val<=le or t.val>=ri:
                return False
            if t.right!=None:
                stack.append([t.right,t.val,ri])
            if t.left!=None:
                stack.append([t.left,le,t.val])
        return True
        # if root.left != None and root.right != None:
        #     if root.left.val < root.val and root.right.val > root.val:
        #         return self.isValidBST(root.left) and self.isValidBST(root.right)
        #     else:
        #         return False
        # elif root.left == None and root.right != None:
        #     if root.right.val > root.val:
        #         return self.isValidBST(root.right)
        #     else:
        #         return False
        # elif root.left != None and root.right == None:
        #     if root.left.val < root.val:
        #         return self.isValidBST(root.left)
        #     else:
        #         return False
        # else:
        #     return True

solution = Solution()

root = TreeNode(2, TreeNode(1), TreeNode(3))
print(solution.isValidBST(root))

root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(solution.isValidBST(root))