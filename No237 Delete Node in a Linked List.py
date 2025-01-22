class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteNode(self, node):
        while node.next != None:
            node.val = node.next.val
            if node.next.next != None:
                node = node.next
            else:
                break
        node.next = None

solution = Solution()

node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
print(solution.deleteNode(node2))

node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
print(solution.deleteNode(node3))
