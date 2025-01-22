
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node=self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val

    def hasNext(self) -> bool:
        return self.stack

root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))

bSTIterator = BSTIterator(root)
bSTIterator.next()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()
bSTIterator.next()
bSTIterator.hasNext()