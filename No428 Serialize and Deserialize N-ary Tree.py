# tranversal of N-ary tree
# 一层父节点带着子节点组成的list
from typing import List

class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

class Serialize_and_Deserialize_N_ary_Tree:
    class Codec:
        # Encodes a tree to a single string.
        def serialize(self, root) -> List:
            if root == None:
                return []
            if root.children:
                val = []
                for child in root.children:
                    val.append(self.serialize(self, child))
                return [root.val, val]
            return root.val

        # Decodes your encoded data to tree.
        def deserialize(self, data) -> 'Node':
            if type(data) == int:
                return Node(data)
            for val in data:
                if type(val) == int:
                    root = Node(val)
                else:
                    for entry in val:
                        root.children.append(self.deserialize(self, entry))
            return root

solution = Serialize_and_Deserialize_N_ary_Tree()
root = Node(1) # [1]
ser = solution.Codec.serialize(solution.Codec, root)
print(ser)
newroot = solution.Codec.deserialize(solution.Codec, ser)

root = Node(1, [Node(3)]) # [1]
ser = solution.Codec.serialize(solution.Codec, root)
print(ser)
newroot = solution.Codec.deserialize(solution.Codec, ser)

root = Node(1, [Node(3), Node(2), Node(4)]) # [1,[3,2,4]]
ser = solution.Codec.serialize(solution.Codec, root)
print(ser)
newroot = solution.Codec.deserialize(solution.Codec, ser)

root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]) # [1,[[3,[5,6]]2,4]]
ser = solution.Codec.serialize(solution.Codec, root)
print(ser)
newroot = solution.Codec.deserialize(solution.Codec, ser)

root = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
ser = solution.Codec.serialize(solution.Codec, root)
print(ser)
newroot = solution.Codec.deserialize(solution.Codec, ser)
print(1)
# [1,
#  [2, [3, [6, [7, [[11, [14]]]]]], [4, [[8, [12]]]], [5, [[9, [13]], 10]]]
#  ]