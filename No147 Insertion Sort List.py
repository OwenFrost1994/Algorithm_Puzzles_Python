class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        if head == None:
            return head
        
        point = head
        while point.next != None:
            if point.val > point.next.val:
                move = point.next
                point.next = move.next
                point = head
                if head.val > move.val:
                    move.next = head
                    head = move
                else:
                    while point.next != None and point.next.val < move.val:
                        point = point.next
                    if point.next == None:
                        point.next = move
                    if point.next.val >= move.val:
                        move.next = point.next
                        point.next = move
                point = head
                continue
            point = point.next

        return head

solution = Solution()

head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
newhead1 = solution.insertionSortList(head1)

head2 = head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
newhead2 = solution.insertionSortList(head2)

head3 = ListNode(4, ListNode(2))
newhead3 = solution.insertionSortList(head3)

head4 = ListNode(4)
newhead4 = solution.insertionSortList(head4)

newhead5 = solution.insertionSortList(None)