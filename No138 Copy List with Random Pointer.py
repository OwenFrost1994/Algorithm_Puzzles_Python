class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None
        visited = {}
        newhead = Node(head.val)
        visited[head] = newhead
        point = head
        while point.next != None:
            node = Node(point.next.val)
            visited[point].next = node
            visited[point.next] = node
            point = point.next
        
        point = head
        while point != None:
            if point.random == None:
                visited[point].random = None
            else:
                visited[point].random = visited[point.random]
            point = point.next

        return newhead
        

solution = Solution()

head1 = Node(7, Node(13, Node(11, Node(10, Node(1)))))
head1.random = None
head1.next.random = head1
head1.next.next.random = head1.next.next.next.next
head1.next.next.next.random = head1.next.next
head1.next.next.next.next.random = head1
newhead1 = solution.copyRandomList(head1)

head2 = Node(1, Node(2))
head2.random = head2.next
head2.next.random = head2.next
newhead2 = solution.copyRandomList(head2)

head3 = Node(3, Node(3, Node(3)))
head3.random = None
head3.next.random = head3
head3.next.next.random = None
newhead3 = solution.copyRandomList(head3)