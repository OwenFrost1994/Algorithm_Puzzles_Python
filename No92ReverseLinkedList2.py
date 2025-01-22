class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        point = head
        if head == None or left == right:
            return head
        listlen = 0
        while(point != None):
            point = point.next
            listlen += 1
        
        nodes = []
        count = 1
        asshead = head
        tail = head
        point = head
        while(count <= right):
            if left != 1 and count == left - 1:
                asshead = point
            if count >= left:
                nodes.append(point)
            point = point.next
            count += 1
        tail = point

        revlist = nodes.pop()
        point = revlist

        while(len(nodes) > 0):
            point.next = nodes.pop()
            point = point.next
        
        if left == 1:
            head = revlist
        else:
            asshead.next = revlist
        point.next = tail
        
        return head
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
print(solution.reverseBetween(head, 2, 4))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
print(solution.reverseBetween(head, 1, 3))

head = ListNode(5)
solution = Solution()
print(solution.reverseBetween(head, 1))
