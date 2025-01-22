class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        return self.addtreenode(head, self.lenth(head))
    
    def addtreenode(self, head, length):
        if length <= 0:
            return None
        
        mid = length // 2
        point = head
        point1 = head
        for i in range(mid):
            if i > 0:
                point1 = point1.next
            point = point.next
        treenode = TreeNode(point.val)
        head1 = point.next
        point = None
        if length > 1:
            point1.next = None
        else:
            head = None

        treenode.left = self.addtreenode(head, self.lenth(head))
        treenode.right = self.addtreenode(head1, self.lenth(head1))

        return treenode
    
    def lenth(self, head):
        if head == None:
            return 0
        
        point = head
        length = 0
        while point != None:
            length += 1
            point = point.next
        return length

solution = Solution()
head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
print(solution.sortedListToBST(head))

head = None
print(solution.sortedListToBST(head))