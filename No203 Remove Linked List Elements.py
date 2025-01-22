class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        if head == None:
            return head
        while head != None and head.val == val:
            head = head.next
        point = head
        while point != None and point.next != None:
            if point.next.val == val:
                point.next = point.next.next
            else:
                point = point.next
        return head

        
solution = Solution()

head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6
print(solution.removeElements(head, val))

head = None
val = 1
print(solution.removeElements(head, val))

head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val = 7
print(solution.removeElements(head, val))