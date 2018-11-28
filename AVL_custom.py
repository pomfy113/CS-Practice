
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

		self.left = None
		self.right = None
		self.height = 0

	def __repr__(self):
		return 'BinaryTreeNode({!r})'.format(self.data)

class AVLTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def is_empty(self):
		return self.root is None


	def insert(self, item):
		# If we're empty, well, that's the parent now
		if self.is_empty():
			self.root = Node(item, 1)
			self.size += 1
			return

		parent, height = self.find_parent(item)
		parent_data = parent.data

		if item == parent_data: # Um.
			return
		elif item > parent_data: # item is more than parent
			parent.right = Node(item)
		elif item < parent_data: # item is less than parent
			parent.left = Node(item)

		self.size+= 1

	def find_parent(self, item):
		node = self.root
		parent = None
		while node is not None:
			content = node.data

			if item == content: # item is... same as parent?
				return parent, height
			elif item > content: # item is more than parent
				parent = node
				node = node.right
			elif item < content: # item is less than parent
				parent = node
				node = node.left

		return parent, height


	def items_in_order(self):
		"""Return an in-order list of all items in this binary search tree."""
		items = []
		if not self.is_empty():
			# Traverse tree in-order from root, appending each node's item
			self._traverse_in_order_recursive(self.root, items.append)
		# Return in-order list of all items in tree
		return items

	def _traverse_in_order_recursive(self, node, visit):
		if node.left is not None:
			self._traverse_in_order_recursive(node.left, visit)
		visit(node.data)
		if node.right is not None:
			self._traverse_in_order_recursive(node.right, visit)

		return visit

	def items_pre_order(self):
		"""Return an in-order list of all items in this binary search tree."""
		items = []
		if not self.is_empty():
			# Traverse tree in-order from root, appending each node's item
			self._traverse_pre_order_recursive(self.root, items.append)
		# Return in-order list of all items in tree
		return items

	def _traverse_pre_order_recursive(self, node, visit):
		visit(node.data)
		if node.left is not None:
			self._traverse_pre_order_recursive(node.left, visit)
		if node.right is not None:
			self._traverse_pre_order_recursive(node.right, visit)
		return visit


items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
print('items: {}'.format(items))

tree = AVLTree()
print('tree: {}'.format(tree))
print('root: {}'.format(tree.root))

print('\nInserting items:')
for item in items:
	tree.insert(item)
	print('insert({}), size: {}\n'.format(item, tree.size))
print('root: {}'.format(tree.root))
print("Inorder", tree.items_in_order())
print("Preorder", tree.items_pre_order())
print(tree)
