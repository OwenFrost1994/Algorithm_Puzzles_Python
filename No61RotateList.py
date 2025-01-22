import collections
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        point = head
        if head == None or k == 0:
            return head
        listlen = 0
        while(point != None):
            point = point.next
            listlen += 1
        
        while k >= listlen:
            k = k - listlen
        if k == 0:
            return head
        
        position = listlen - k
        asspoint = head
        point = head
        count = 0
        while(count < position - 1):
            asspoint = asspoint.next
            count += 1
        nodes = collections.deque()
        point = asspoint.next
        while(point != None):
            nodes.append(point)
            point = point.next
            count += 1
        asspoint.next = None
        asshead = nodes.popleft()
        point = asshead
        while(len(nodes)>0):
            point.next = nodes.popleft()
            point = point.next
        point.next = head
        return asshead

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
print(solution.rotateRight(head, 2))

head = ListNode(0, ListNode(1, ListNode(2)))
solution = Solution()
print(solution.rotateRight(head, 4))

head = ListNode(1)
solution = Solution()
print(solution.rotateRight(head, 1))