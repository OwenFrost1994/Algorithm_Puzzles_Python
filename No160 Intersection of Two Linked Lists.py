class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
class Solution:
    def getIntersectionNode(self, headA, headB):
        nodeA = []
        nodeB = []

        while headA != None:
            nodeA.append(headA)
            headA = headA.next
        while headB != None:
            nodeB.append(headB)
            headB = headB.next
        
        node = None
        while nodeA and nodeB:
            node1 = nodeA.pop()
            node2 = nodeB.pop()
            if node1 != node2:
                return node
            node = node1
        return None

solution = Solution()

headA = ListNode(4, ListNode(1))
headB = ListNode(5, ListNode(6, ListNode(1)))
HeadC = ListNode(8, ListNode(4, ListNode(5)))

headA.next.next = HeadC
headB.next.next.next = HeadC
print(solution.getIntersectionNode(headA, headB) == HeadC)
