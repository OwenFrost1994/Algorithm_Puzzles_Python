class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # process head nodes
        if (head == None or head.next == None):
            return head
        point1 = head.next
        point2 = head
        while point2.val == point1.val:
            head = point1
            if point1.next != None and point1.next.val != point1.val:
                head = point1.next
                point2 = head
                if head.next == None:
                    return head
                else:
                    point1 = head.next
                    continue
            if point1.next == None:
                return None
            point1 = head.next
            point2 = head
        
        while point1 != None:
            if point1.next != None and point1.next.val == point1.val:
                deleteval = point1.val
                while(point1.val == deleteval):
                    point1 = point1.next
                    point2.next = point1
                    if point1 == None:
                        return head
            if point1.next != None and point1.next.val != point1.val:
                point2 = point1
                point1 = point1.next
            if point1.next == None:
                break
        return head
            



head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))))
solution = Solution()
print(solution.deleteDuplicates(head))
head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
solution = Solution()
print(solution.deleteDuplicates(head))