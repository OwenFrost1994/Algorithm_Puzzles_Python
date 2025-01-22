class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        point = head
        nums = []
        while(point != None):
            nums.append(point.val)
            point = point.next
        nums.sort(reverse = False)
        point = head
        i = 0
        while(point != None):
            point.val = nums[i]
            point = point.next
            i += 1
        return head

solution = Solution()
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
head = solution.sortList(head)

head = ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5)))))
head = solution.sortList(head)