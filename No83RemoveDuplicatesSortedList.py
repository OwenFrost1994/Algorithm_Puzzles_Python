class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        point1 = head
        point2 = head.next
        while point2 != None:
            while point2 != None and point2.val == point1.val :
                point2 = point2.next
                point1.next = point2
            if point2 != None:
                point2 = point2.next
            point1 = point1.next
        return head
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
solution = Solution()
print(solution.deleteDuplicates(head))
head = ListNode(1, ListNode(1, ListNode(2)))
solution = Solution()
print(solution.deleteDuplicates(head))