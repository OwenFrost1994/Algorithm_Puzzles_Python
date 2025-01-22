# Since the tree is a binary search tree, there is no need to look up any of the node’s values.
# If the node has a right child, then obtain the leftmost node in the current node’s left subtree, 
# which is the in-order success of the current node.
# If the node doesn’t have a right child, then the node has an in-order successor if and only if there 
# is another node such that the current node is in another node’s left subtree. Starting from the current node, 
# find each node’s parent. If there exist a (parent, child) pair such that the child is the parent’s left child, then return the parent. If such a parent is not found, return null.
# Definition for a Node.
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> Optional[Node]:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

