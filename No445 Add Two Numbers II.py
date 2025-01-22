# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        s1 = []
        s2 = []
        pointer = l1
        while pointer != None:
            s1.append(pointer.val)
            pointer = pointer.next
        pointer = l2
        while pointer != None:
            s2.append(pointer.val)
            pointer = pointer.next
        carry, dummy = 0, ListNode()
        while s1 or s2 or carry:
            carry += (0 if not s1 else s1.pop()) + (0 if not s2 else s2.pop())
            carry, val = divmod(carry, 10)
            node = ListNode(val, dummy.next)
            dummy.next = node
        return dummy.next

solution = Solution()
print(solution.addTwoNumbers(l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3)))), l2 = ListNode(5, ListNode(6, ListNode(4)))))
print(solution.addTwoNumbers(l1 = ListNode(2, ListNode(4, ListNode(3))), l2 = ListNode(5, ListNode(6, ListNode(4)))))
print(solution.addTwoNumbers(l1 = ListNode(0), l2 = ListNode(0)))