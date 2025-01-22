class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        stack = []
        point = head
        while point != None:
            stack.append(point)
            point = point.next
        digit = 0
        node = stack.pop()
        node.val += 1
        if node.val >= 10:
            digit = 1
            node.val -= 10
        while digit and stack:
            node = stack.pop()
            node.val += digit
            if node.val >= 10:
                digit = 1
                node.val -= 10
            else:
                digit = 0
        if digit == 1 and len(stack) == 0:
            head = ListNode(1, head)
        return head

solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3)))
head = solution.plusOne(head)
head = ListNode(0)
head = solution.plusOne(head)
head = ListNode(8, ListNode(9, ListNode(9)))
head = solution.plusOne(head)
head = ListNode(9, ListNode(9, ListNode(9)))
head = solution.plusOne(head)