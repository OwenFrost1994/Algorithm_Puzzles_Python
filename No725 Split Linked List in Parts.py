class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        listlen = 0
        point = head
        while point != None:
            point = point.next
            listlen += 1
        sublen = listlen // k
        residual = listlen % k
        heads = []
        point = head
        for i in range(k):
            lenth = sublen
            if residual > 0:
                lenth += 1
                residual -= 1
            subhead = point
            if point != None:
                end = point
                for j in range(lenth):
                    if j > 0:
                        end = end.next
                    point = point.next
                end.next = None
            heads.append(subhead)
        return heads
solution = Solution()
head = None
heads = solution.splitListToParts(head, 2)
head = ListNode(1, ListNode(2, ListNode(3)))
heads = solution.splitListToParts(head, 5)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
heads = solution.splitListToParts(head, 2)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
heads = solution.splitListToParts(head, 3)