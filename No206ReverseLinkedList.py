class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        point1 = head.next
        point2 = head
        point3 = head.next.next
        point2.next = None
        while(point1 != None):
            point1.next = point2
            point2 = point1
            point1 = point3
            if point3 != None:
                point3 = point3.next
        return point2

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
head = solution.reverseList(head)
point = head
while point != None:
    print(point.val)
    point = point.next

head = ListNode(1, ListNode(2))
head = solution.reverseList(head)
point = head
while point != None:
    print(point.val)
    point = point.next