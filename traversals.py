# example inorder, preorder, and postorder traversals


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time to evaluate each node in the tree
# O(n) space call stack
def preorder(node):
    # evaluate this node
    print(node.value)
    # traverse left
    if node.left:
        preorder(node.left)
    # traverse right
    if node.right:
        preorder(node.right)


# O(n) time to evaluate each node in the tree
# O(n) space call stack
def inorder(node):
    # traverse left
    if node.left:
        inorder(node.left)
    # evaluate this node
    print(node.value)
    # traverse right
    if node.right:
        inorder(node.right)


# O(n) time to evaluate each node in the tree
# O(n) space call stack
def postorder(node):
    # traverse left
    if node.left:
        postorder(node.left)
    # traverse right
    if node.right:
        postorder(node.right)
    # evaluate this node
    print(node.value)


# testing tree
#       A
#   B       C
# D   E   F   G

root = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
root.left = B
root.right = C
B.left = D
B.right = E
C.left = F
C.right = G

preorder(root)  # ABDECFG
inorder(root)  # DBEAFCG
postorder(root)  # DEBFGCA
