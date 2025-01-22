# class Solution:
#     def __init__(self, head: Optional[ListNode]):
#         self.head = head

#     def getRandom(self) -> int:
#         n = ans = 0
#         head = self.head
#         while head:
#             n += 1
#             x = random.randint(1, n)
#             if n == x:
#                 ans = head.val
#             head = head.next
#         return ans
import random
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head):
        self.head = head
        n = 0
        pointer = head
        while pointer:
            n += 1
            pointer = pointer.next
        self.len = n

    def getRandom(self) -> int:
        index = random.randint(1, self.len)
        pointer = self.head
        num = 0
        while pointer:
            num += 1
            if num == index:
                return pointer.val
            pointer = pointer.next
        
head = ListNode(1, ListNode(2, ListNode(3)))
solution = Solution(head)
print(solution.getRandom()) # return 1
print(solution.getRandom()) # return 3
print(solution.getRandom()) # return 2
print(solution.getRandom()) # return 2
print(solution.getRandom()) # return 3
