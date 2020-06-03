import random
# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# A utility function to insert a new node with the given key
def insertSorted(root, node):
    if root is None:
        root = node
        print(root.value)
    else:
        if node.value > root.value:
            if root.right is None:
                root.right = node
            else:
                insertSorted(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertSorted(root.left, node)

def insert(root, node):
    if root is None:
        root = node
        print(root.value)
    else:
        choice = random.choice([True, False])
        if choice:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def print_tree(current_node, nameattr='value', left_child='left', right_child='right', indent='', last='updown'):

    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    up = getattr(current_node, left_child)
    down = getattr(current_node, right_child)

    if up is not None:
        next_last = 'up'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str(name(current_node))))
        print_tree(up, nameattr, left_child, right_child, next_indent, next_last)

    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up is not None and down is not None: end_shape = '┤'
    elif up: end_shape = '┘'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

    if down is not None:
        next_last = 'down'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '|', ' ' * len(str(name(current_node))))
        print_tree(down, nameattr, left_child, right_child, next_indent, next_last)

