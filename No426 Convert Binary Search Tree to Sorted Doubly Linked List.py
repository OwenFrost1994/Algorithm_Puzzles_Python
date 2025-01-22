# 一开始没想明白，根本原因是没有搞懂树的问题，首先要想怎么遍历：前序、中序还是后序？
# binary search tree 从中间提升一个值构成节点，两边继续向下分，最小的一定在左边，需要前序遍历
# linked list 无论 single 还是 double 都需要找到头结点和前一节点然后往后连接
# 1<-2->3, 先到节点1，这时候prev是空，head就直接到节点1，prev节点就是1，退到2，前驱节点prev不为空，连接prev和当前节点，前驱节点更新到本节点
# 之后遍历到3,前驱节点连接3,更新到3
# (1<-2->3)<-4->(5<-6->7), 走完了3以后连接3和4，再走另一个子树
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        head = None # global variables
        prev = None
        def dfs(root):
            if root == None:
                return
            nonlocal prev, head
            dfs(root.left)
            if prev:
                prev.right = root
                root.left = prev
            else:
                head = root
            prev = root
            dfs(root.right)
        
        if root == None:
            return None
        head = prev = None
        dfs(root)
        head.left = prev
        prev.right = head
        return head
solution = Solution()
root = None
newroot = solution.treeToDoublyList(root)
root = Node(2, Node(1), Node(3))
newroot = solution.treeToDoublyList(root)
root = Node(4, Node(2, Node(1), Node(3)), Node(5))
newroot = solution.treeToDoublyList(root)
print(1)