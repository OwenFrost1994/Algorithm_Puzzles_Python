from collections import deque
def printtree(root):
    nodes = deque()
    value = deque()
    nodes.append(root)
    while nodes:
        n = len(nodes)
        for _ in range(n):
            node = nodes.popleft()
            if node != None:
                value.append(node.val)
            else:
                value.append("None")
                continue
            if node.left != None:
                nodes.append(node.left)
            else:
                if node.right != None:
                    nodes.append(None)
            if node.right != None:
                nodes.append(node.right)
            else:
                if node.right != None:
                    nodes.append(None)
    print(value)