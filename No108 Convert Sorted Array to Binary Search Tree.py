class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        return self.addtreenode(0, len(nums) - 1, nums)
    
    def addtreenode(self, left, right, nums):
        if left > right:
            return None
        
        mid = (left + right)//2
        treenode = TreeNode(nums[mid])
        
        treenode.left = self.addtreenode(left, mid - 1, nums)
        treenode.right = self.addtreenode(mid + 1, right, nums)

        return treenode

solution = Solution()

nums = [-10,-3,0,5,9]
print(solution.sortedArrayToBST(nums))

nums = [1,3]
print(solution.sortedArrayToBST(nums))