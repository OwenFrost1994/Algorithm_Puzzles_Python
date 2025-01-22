class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """
        stack = []
        stack.append(root)
        series = ""
        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if node:
                    series += str(node.val) + " "
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    series += "#" + " "
        return series[:-1]

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        datas = data.split(" ")
        stack = []
        if datas[0] != "#":
            root = TreeNode(int(datas.pop(0)))
        else:
            return None
        stack.append(root)
        while datas:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if not node:
                    continue
                l = datas.pop(0)
                r = datas.pop(0)
                if l != "#":
                    node.left = TreeNode(l)
                    stack.append(node.left)
                else:
                    node.left = None
                if r != "#":
                    node.right = TreeNode(r)
                    stack.append(node.right)
                else:
                    node.right = None
        return root

ser = Codec()
deser = Codec()
root = TreeNode(2, TreeNode(1), TreeNode(3))
tree = ser.serialize(root)
ans = deser.deserialize(tree)
root = None
tree = ser.serialize(root)
ans = deser.deserialize(tree)