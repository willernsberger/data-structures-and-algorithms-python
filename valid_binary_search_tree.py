# given the root of a tree, determine if the tree is a valid binary search tree
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# valid binary search tree all left descendants are less than or equal to its
# parent and all right descendants are greater than its parent
# depth first traversal
# linear time (must search every node)
# linear space (wort case stack depth is number of nodes)
def valid_binary_search_tree(node):
    ceiling = math.inf
    floor = -math.inf
    # evaluate the node
    if node.left and node.left.value > node.value:
        return False
    if node.right and node.right.value < node.value:
        return False
    # traverse left, passing the ceiling
    if node.left:
        if not traversal(node.left, min(ceiling, node.value), floor):
            return False
    # traverse right, passing the floor
    if node.right:
        if not traversal(node.right, ceiling, max(floor, node.value)):
            return False
    return True


# helper function for the traversal
def traversal(node, ceiling, floor):
    # evaluate the node
    if node.value >= ceiling or node.value <= floor:
        return False
    if node.left and node.left.value > node.value:
        return False
    if node.right and node.right.value < node.value:
        return False
    # traverse left, updating the the ceiling
    if node.left:
        if not traversal(node.left, min(ceiling, node.value), floor):
            return False
    # traverse right, updating the floor
    if node.right:
        if not traversal(node.right, ceiling, max(floor, node.value)):
            return False
    return True


# test data
#
#     50
#    /  \
#   25  100
#  / \   / \
# 10 30 75  200

root = Node(50)
root.left = Node(25)
root.right = Node(100)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(75)
root.right.right = Node(200)


# driver
print(valid_binary_search_tree(root))
