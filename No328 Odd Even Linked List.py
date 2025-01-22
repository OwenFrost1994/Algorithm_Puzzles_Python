class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if head == None or head.next == None:
            return head
        pointp = head
        pointe = head.next
        even = pointe
        while pointe != None:
            pointp.next = pointe.next
            if pointe.next != None:
                pointe.next = pointe.next.next
            if pointp.next != None:
                pointp = pointp.next
            pointe = pointe.next
        pointp.next = even
        return head
solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
newhead = solution.oddEvenList(head)
head = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
newhead = solution.oddEvenList(head)