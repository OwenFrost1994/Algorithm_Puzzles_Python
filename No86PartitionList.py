class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        greater = []
        smaller = []
        point = head
        while(point != None):
            if point.val >= x:
                greater.append(point.val)
            else:
                smaller.append(point.val)
            point = point.next
        i = 0
        point = head
        while(point != None):
            if i < len(smaller):
                point.val = smaller[i]
            else:
                point.val = greater[i - len(smaller)]
            point = point.next
            i += 1
        return head

solution = Solution()
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
head = solution.partition(head, x)

head = ListNode(2, ListNode(1))
x = 2
head = solution.partition(head, x)