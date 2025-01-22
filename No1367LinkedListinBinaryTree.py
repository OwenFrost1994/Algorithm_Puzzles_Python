class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head, root):
        return self.recurtree(head, root)
    
    def recurtree(self, head, treenode):
        if head.val == head.val and self.recurlist(head, treenode):
            return True
        if treenode.left != None:
            left = self.recurtree(head, treenode.left)
        else:
            left = False
        if treenode.right != None:
            right = self.recurtree(head, treenode.right)
        else:
            right = False
        return right or left
    
    def recurlist(self, node, treenode):
        if node == None:
            return True
        if treenode == None or treenode.val != node.val:
            return False
        return self.recurlist(node.next, treenode.left) or self.recurlist(node.next, treenode.right)

solution = Solution()
head = ListNode(4, ListNode(2, ListNode(8)))
root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1), None)), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3))), None))
print(solution.isSubPath(head, root))

head = ListNode(1, ListNode(4, ListNode(2, ListNode(6))))
print(solution.isSubPath(head, root))

head = ListNode(1, ListNode(4, ListNode(2, ListNode(6, ListNode(8)))))
print(solution.isSubPath(head, root))