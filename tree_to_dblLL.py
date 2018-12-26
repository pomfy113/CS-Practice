from AVL_starter import BinarySearchTree

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return '[ NODE - {}, nxt-{}, prv-{} ]'.format(self.data,\
         '[node-{}]'.format(self.next.data) if self.next else 'N/A',\
         '[node-{}]'.format(self.prev.data) if self.prev else 'N/A')

def change_to_LL(tree):
    node = tree.root
    items = []
    in_order(node, items.append)
    return items


def in_order(node, visit):
    if node is None:
        return

    in_order(node.left, visit)
    visit(Node(node.data))
    in_order(node.right, visit)


tree = BinarySearchTree()

for i in range(1, 8):
    tree.insert_new(i)


LL = []
items = change_to_LL(tree)
prev = None

for node in items:
    if prev is not None:
        prev.next = node
        node.prev = prev
    prev = node

print(items)
