# 一个方法是stack method，这个栈存储前面的list还没走完的头节点
# Definition for a Node.
class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        if head == None:
            return head
        stack = []
        pointer = head
        while (pointer.next != None or stack) or pointer.child != None:
            if pointer.child != None:
                if pointer.next != None:
                    stack.append(pointer.next)
                pointer.next = pointer.child
                pointer.next.prev = pointer
                pointer.child = None
            if pointer.next == None and stack:
                pointer.next = stack.pop()
                pointer.next.prev = pointer
            pointer = pointer.next
        return head

solution = Solution()
root = None
newroot = solution.flatten(root)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node1.next = Node2
Node2.prev = Node1
Node1.child = Node3
newroot = solution.flatten(Node1)
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node1.next = Node2
Node2.prev = Node1
Node2.child = Node3
newroot = solution.flatten(Node1)

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)
Node10 = Node(10)
Node11 = Node(11)
Node12 = Node(12)
Node13 = Node(13)

Node1.next = Node2
Node2.prev = Node1
Node2.next = Node3
Node3.prev = Node2
Node3.next = Node4
Node4.prev = Node3
Node4.next = Node5
Node5.prev = Node4
Node5.next = Node6
Node6.prev = Node5

Node7.next = Node8
Node8.prev = Node7
Node8.next = Node9
Node9.prev = Node8
Node9.next = Node10
Node10.prev = Node9

Node11.next = Node12
Node12.prev = Node11
Node12.next = Node13
Node13.prev = Node12

Node3.child = Node7
Node8.child = Node11

newroot = solution.flatten(Node1)