# given a tree and a "clone tree" with a symmetric hierarchy, and a node within the tree,
# find the matching node in the clone tree

# Node class
class Node(object):
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        if self.value:
            return self.value
        else:
            return 'None'


def find_clone(root, clone, given):
    # traverse the original tree and clone tree at the same time
    # evaluate the node at each stop in the traversal
    # if the node is the given node, return the clone

    # preorder traversal
    if root.value == given.value:
        return clone
    # traverse left
    if root.left:
        left = find_clone(root.left, clone.left, given)
        if left:
            return left
    # traverse right
    if root.right:
        right = find_clone(root.right, clone.right, given)
        if right:
            return right


# create the tree, clone tree, and given node for testing
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.right.right = Node('D')
root.right.left = Node('E')

given = root.right.left

clone = Node('F')
clone.left = Node('G')
clone.right = Node('H')
clone.right.right = Node('I')
clone.right.left = Node('J')

# driver function
print(str(str(find_clone(root, clone, given))))  # 'J'
