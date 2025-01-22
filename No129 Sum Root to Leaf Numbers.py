class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def sumNumbers(self, root):
#         self.paths = []
#         self.seachpath(root, [])
#         sum = []
#         return None
    
#     def seachpath(self, root, path):
#         if root == None:
#             return
#         if root.left == None and root.right == None:
#                 path.append(root.val)
#                 self.paths.append(path.copy())
#                 return
#         else:
#             path.append(root.val)
#             if root.left != None:
#                 self.seachpath(root.left, path.copy())
#             if root.right != None:
#                 self.seachpath(root.right, path.copy())
#         path.pop()

class Solution:
    def sumNumbers(self, root):
        def dfs(cur,num):
            if not cur:return 0
            
            num=num*10+cur.val
            
            if not cur.left and not cur.right:
                return num
            
            return dfs(cur.left,num)+dfs(cur.right,num)
        
        return dfs(root,0)
    
solution = Solution()
head = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.sumNumbers(head))

head = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(solution.sumNumbers(head))