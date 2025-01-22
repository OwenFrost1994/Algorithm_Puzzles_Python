class TreeNode(object):
    def __init__(self, x, node1 = None, node2 = None):
        self.val = x
        self.left = node1
        self.right = node2

class Codec:
    def serialize(self, root):
        series = ""
        que = []
        que.append(root)
        while que:
            node = que.pop(0)
            if node == None:
                series += "#,"
            else:
                series += str(node.val) + ","
            if node != None:
                que.append(node.left)
                que.append(node.right)
        return series[:-1]

    def deserialize(self, data):
        val = data.split(",")
        if val[0] != "#":
            root = TreeNode(val.pop(0))
        else:
            return None
        que = []
        que.append(root)
        while val:
            nodenum = len(que)
            for i in range(nodenum):
                node = que.pop(0)
                left = val.pop(0)
                right = val.pop(0)
                if left == "#":
                    node.left = None
                else:
                    node.left = TreeNode(left)
                    que.append(node.left)
                if right == "#":
                    node.right = None
                else:
                    node.right = TreeNode(right)
                    que.append(node.right)
        return root
root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(4), TreeNode(5)))
codec = Codec()
rootseries = codec.serialize(root)
print(rootseries)
newroot = codec.deserialize(rootseries)