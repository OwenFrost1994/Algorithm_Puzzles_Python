class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Codec:
#     # Encodes an n-ary tree to a binary tree.
#     def encode(self, root: Node) -> Node:
#         if not root:
#             return None

#         ans = TreeNode(root.val)

#         curr = ans

#         for child in root.children:
#             curr.left = self.encode(child)
#             curr.right = TreeNode()
#             curr = curr.right

#         return ans
	
# 	# Decodes your binary tree to an n-ary tree.
#     def decode(self, data: Node) -> Node:
#         if not data:
#             return None

#         children = []

#         ans = Node(data.val,children)

#         curr = data

#         while curr.left:
#             children.append(self.decode(curr.left))
#             curr = curr.right 

#         return ans

class Codec:
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return
        ans = TreeNode(root.val)
        if root.children:
            children = list(map(self.encode, root.children))
            ans.right = children[0]
            for i in range(len(children)-1):
                children[i].left = children[i+1]
        return ans
        
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return
        ans = Node(data.val, [])
        if data.right:
            n = data.right
            while n:
                ans.children.append(self.decode(n))
                n = n.left
        return ans  
solution = Codec()
root = Node(1,[]) # [1]
newroot = solution.encode(root)
newroot = solution.decode(newroot)

root = Node(1, [Node(3, [])]) # [1]
newroot = solution.encode(root)
newroot = solution.decode(newroot)

root = Node(1, [Node(3, []), Node(2, []), Node(4, [])]) # [1,[3,2,4]]
newroot = solution.encode(root)
newroot = solution.decode(newroot)

root = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])]) # [1,[[3,[5,6]]2,4]]
newroot = solution.encode(root)
newroot = solution.decode(newroot)

root = Node(1, [Node(2, []), Node(3, [Node(6, []), Node(7, [Node(11, [Node(14, [])])])]), Node(4, [Node(8, [Node(12, [])])]), Node(5, [Node(9, [Node(13, [])]), Node(10, [])])])
newroot = solution.encode(root)
newroot = solution.decode(newroot)
print(1)