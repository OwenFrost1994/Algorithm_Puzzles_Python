class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# class Solution:
#     paths = []
#     def pathSum(self, root, targetSum):
#         self.paths = []
#         self.seachpath(root, 0, [], targetSum)
#         unipath = []
#         for sublist in self.paths:
#             if sublist not in unipath:
#                 unipath.append(sublist)
#         return len(unipath)
    
#     def seachpath(self, root, sum, path, targetSum):
#         if root == None:
#             return
#         if sum + root.val == targetSum:
#                 path.append(root.val)
#                 self.paths.append(path.copy())
#         else:
#             path.append(root.val)
#             if root.left != None:
#                 self.seachpath(root.left, sum + root.val, path, targetSum)
#                 self.seachpath(root.left, 0, [], targetSum)
#             if root.right != None:
#                 self.seachpath(root.right, sum + root.val, path, targetSum)
#                 self.seachpath(root.right, 0, [], targetSum)
#         path.pop()

class Solution:
    def pathSum(self, root, targetSum):
        self.count = 0
        def sum(node, targetSum):
            if node is None:
                return 
            elif node.val==targetSum:
                self.count+=1
            sum(node.left, targetSum-node.val)
            sum(node.right, targetSum-node.val)
        def dfs(node, target):
            if node is None:
                return 
            sum(node, target)
            dfs(node.left, target)
            dfs(node.right,target)
        dfs(root, targetSum)
        return self.count
    
solution = Solution()
# head = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
# print(solution.pathSum(head, 8))

head = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1), None), TreeNode(3)), TreeNode(-3, TreeNode(-2), None))
print(solution.pathSum(head, 3))