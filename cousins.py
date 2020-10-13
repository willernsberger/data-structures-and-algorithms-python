# Given a binary tree and a node in that tree, find the number of "cousins".
# A node is considered a cousin if it is of the same depth but does not
# share the same parent node.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.value)


class Solution(object):
    def __init__(self, root, node):
        self.cousins = []
        self.depth = 0
        self.root = root
        self.node = node
        self.parent = None

    # Two pass algorithm.  First, traverse the tree to find the depth
    # and parent of the given node.  Second, traverse the tree returning each
    # node of the given depth which does not share a common parent.
    # Linear time complexity for each pass, for a total time complexity
    # of linear with respect to the number of nodes in the tree.
    # Linear space complexity with respect to the number of nodes in the
    # tree as the the worst-case call stack for a depth first traversal
    # is the number of nodes in the tree.
    def find_the_cousins(self):
        self.find_depth_and_parent()
        self.find_cousins()
        return self.cousins

    # bootstrap the traversal to find the depth and parent of the given node
    def find_depth_and_parent(self):
        self.find_depth_and_parent_helper(self.root, 0, None)

    # preorder traversal to find the depth of the given node
    def find_depth_and_parent_helper(self, node, depth, parent):
        # evaluate
        if node.value == self.node.value:
            self.depth = depth
            self.parent = parent
            return
        # traverse left
        if node.left:
            self.find_depth_and_parent_helper(node.left, depth + 1, node)
        # traverse right
        if node.right:
            self.find_depth_and_parent_helper(node.right, depth + 1, node)

    # bootstrap the traversal to find the cousins
    def find_cousins(self):
        self.find_cousins_helper(self.root, 0)

    # preorder traversal to find the cousins
    def find_cousins_helper(self, node, depth, parent=None):
        # evaluate
        if depth == self.depth and not parent:
            return
        if depth == self.depth and parent.value != self.parent.value:
            self.cousins.append(node)
            return
        # traverse left
        if node.left:
            self.find_cousins_helper(node.left, depth + 1, node)
        # traverse right
        if node.right:
            self.find_cousins_helper(node.right, depth + 1, node)


# testing node and tree
#    1
#  2   3
# 4 5 6 7
#
input_root = Node(1)
input_root.left = Node(2)
input_root.right = Node(3)
input_root.left.left = Node(4)
input_root.left.right = Node(5)
input_node = Node(7)
input_root.right.left = Node(6)
input_root.right.right = input_node

# driver
s = Solution(input_root, input_node)
print(s.find_the_cousins())  # [4, 5]
