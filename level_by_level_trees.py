from collections import deque


# given a tree, print the nodes in the tree
# with a new line for each level
# O(n) runtime complexity, evaluating each node once
# O(1) space complexity, only a few variables for state
class Node(object):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def __repr__(self):
        if self.value:
            return str(self.value)
        return 'Node does not have a value.'


def print_level_by_level(node):
    # create a queue, add root to the queue
    q = deque([node])
    counter = 1
    children_counter = 0
    # breadth first traversal
    while len(q):
        node = q.popleft()
        counter -= 1
        print(node, end='')
        for child in node.children:
            q.append(child)
            children_counter += 1
        if counter == 0:
            print('')
            counter = children_counter


root = Node('a', [])
root.children.append(Node('b', []))
root.children.append(Node('c', []))
root.children[1].children.append(Node('d', []))
root.children[1].children.append(Node('e', []))
root.children[1].children.append(Node('f', []))

print_level_by_level(root)