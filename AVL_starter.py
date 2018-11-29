#!python

from collections import deque

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        if (self.left is None) and (self.right is None):
            return True
        else:
            return False

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        if (self.left is None) and (self.right is None):
            return False
        else:
            return True

    def is_1branch(self):
        if self.left is None and self.right is not None:
            return True
        elif self.left is not None and self.right is None:
            return True
        else:
            return False

    def is_2branch(self):
        if self.left is not None and self.right is not None:
            return True
        else:
            return False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Runtime: Constant if 1 object, n due to looking at everything.
        """
        # Check if left child has a value and if so calculate its height
        left_height = right_height = 0
        if self.is_leaf():
            return 0
        if self.left is not None:
            node = self.left
            left_height = node.height() + 1
        # Check if right child has a value and if so calculate its height
        if self.right is not None:
            node = self.right
            right_height = node.height() + 1
        # Return one more than the greater of the left height and right height
        return max(right_height, left_height)

class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert_new(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        n; going to go through everything"""
        # TODO: Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        log(n): it's going to traverse based on height, which is log(n) """
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        log(n): it's going to traverse based on height, which is log(n)"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree. If it's empty,
        well, it's 1. Otherwise, log(n); we know where we're heading."""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Grab parent of where node should be
        parent = self._find_parent_node(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)

        self.size += 1

    def insert_new(self, item):
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        print("CURRENT:", self.items_level_order())
        self._insert_helper(item)
        self.size += 1
        print("NEW", self.items_level_order())

        print("DONE\n\n\n\n")
        pass

    def _insert_helper(self, item, node=None):
        # Init
        if node is None:
            child = self._insert_helper(item, self.root)
            if child is not None:
                self._balance(node, child)

        elif item < node.data: # Left child
            if node.left is None:
                node.left = BinaryTreeNode(item)
                print("INSERTING", item)
                return node
            else:
                child = self._insert_helper(item, node.left)
                if child is not None:
                    self._balance(node, child)
                return node

        elif item > node.data: # Right child
            if node.right is None:
                node.right = BinaryTreeNode(item)
                print("INSERTING", item)
                return node
            else:
                child = self._insert_helper(item, node.right)
                if child is not None:
                    self._balance(node, child)
                return node
        else:
            return

    def _check_balance(self, parent, child):
        left_height = -1
        right_height = -1
        if parent and parent.left:
            left_height = parent.left.height()
        if parent and parent.right:
            right_height = parent.right.height()
        return left_height - right_height

    def _balance(self, parent, child):
        balance = self._check_balance(parent, child)

        if balance < -1:
            # check for additional rotate
            if self._check_balance(child, child.left) >= 1:
                new_child = self._right_rotate(child, child.left)
                parent.right = new_child
                child = new_child
                print(self.items_level_order())


            if parent is not self.root:
                grandparent = self._find_parent_node(parent.data)
                grandparent.right = self._left_rotate(parent, child)

            else:
                print("NON-ROOT", self.items_level_order())
                print(parent, parent.right, child, child.right)
                self.root = self._left_rotate(parent, child)

                print(self.items_level_order())


        elif balance > 1:
            print("Let's not touch this for a bit")
            if parent is not self.root:
                parent.right = self._right_rotate(parent, child)
            elif parent and child is parent.right:
                self.root = self._right_rotate(parent, child)
        return

    def _left_rotate(self, parent, child):
        parent.right = child.left
        child.left = parent


        return child


    def _right_rotate(self, parent, child):
        print(parent)

        parent.left = child.right
        child.right = parent
        print("IN ROTATE", self.items_level_order())
        print(parent, parent.left, parent.right)
        print(child, child.left, child.right)
        return child

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        O(log(n)); the find_node goes through a certain series, so we only
        need to go a certain distance."""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node(self, item, node=None):
        """Recursive version.

        Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        O(log(n)); the find_node goes through a certain series, so we only
        need to go a certain distance."""
        # Start with the root node
        if node is None:
            node = self.root
            # Check if the given item matches the node's data
        if item == node.data:
            # Return the found node
            return node
        elif node.is_leaf():
            return None
        # Check if the given item is less than the node's data
        elif item < node.data and node.left is not None:
            # Descend to the node's left child
            return self._find_node(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data and node.right is not None:
            # Descend to the node's right child
            return self._find_node(item, node.right)


    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Also log(n); we traverse height"""
        # Start with the root node and keep track of its parent
        if self.contains(item):
            return
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node(self, item, node=None, parent=None):
        """Recursive version.

        Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        O(log(n)); the find_node goes through a certain series, so we only
        need to go a certain distance."""
        # Start with the root node
        if node is None:
            node = self.root
            # Check if the given item matches the node's data
        if item == node.data:
            # Return the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data and node.left is not None:
            # Descend to the node's left child
            return self._find_parent_node(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data and node.right is not None:
            # Descend to the node's right child
            return self._find_parent_node(item, node.right, node)
        else:
            return node

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n); we have to go through all of the nodes anyway?
        Memory usage: O(height); call stack goes that far before doing visits
        """
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

        return visit


    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n); we have to go through all of the nodes anyway
        Memory usage: O(height?) We do queue all of the left node"""

        stack = deque()
        stack.enqueue_front(node)
        # I'm going to need a blackboard for this
        while stack.length() > 0:
            # Go as left as possible!
            while node.left is not None:
                stack.enqueue_front(node.left)
                node = node.left
            # If there's no more left, let's pop something + append
            else:
                node = stack.pop_left()
                visit(node.data)
                # Check right and eventually see if it has lefts
                # If it doesn't have a left, we skip the above while loop
                if node.right:
                    stack.append_left(node.right)
                    node = node.right
        return



    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n); ALL the nodes!
        Memory usage: A lot smaller? Like, 1 due to the call stack?
        """
        # Visit this node's data with given function
        visit(node.data)
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

        return

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n forever man)
        Memory usage: Depends on a diagonal; no clue how to calculate this"""
        # Traverse pre-order without using recursion (stretch challenge)
        # [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        stack = DeQueue()
        stack.enqueue_front(node)
        # I'm going to need a blackboard for this
        # while stack.length() > 0:
        #     while node.left is not None:
        #         stack.enqueue_front(node)
        #         node = node.left
        #         visit.append(node.data)
        #     else:
        #         node = stack.dequeue_front()
        #         if node.right:
        #             node = node.right
        #             visit.append(node.data)
        #
        # Above was close, but kept printing the root's right at the end!

        while stack.length() > 0:
            # Keep popping the first thing that shows up!
            node = stack.dequeue_front()
            visit(node.data)
            # We need to make sure we add the right first before left
            # This is to make sure the leftmost is stacked/printed last
            if node.right:
                stack.enqueue_front(node.right)
            if node.left:
                stack.enqueue_front(node.left)
            # Because of this order, this prints what's IMMEDIATELY left
            # then go deeper left before going right
        return

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) forever
        Memory usage: n? It goes through ALL of them first before visiting"""
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # Visit this node's data with given function
        visit(node.data)
        return

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n)
        Memory usage: Half of the tree. It goes down one half before another
        """
        # Traverse post-order without using recursion (stretch challenge)
        # stack = DeQueue()

        # while (stack.length() > 0) or (node):
        #     if node:
        #         stack.enqueue_front(node)
        #         node = node.left
        #     else:
        #         check = stack.front()
        #         if (check.right is not None) and (parent is not check.right):
        #             node = check.right
        #         else:
        #             visit.append(check.data)
        #             parent = stack.dequeue_front()
        # # # # # # # # # # # # # # # # # # # # # #
        # while (stack.length() > 0):
        #     print(stack.list)
        #     while node.right:
        #         if node.right:
        #             stack.enqueue_front(node.right)
        #         node = node.right
        #     else:
        #         if stack.front().left:
        #             node = stack.front().left
        #         else:
        #
        # # # # # # # # # # # # # # # #
        # while(stack.length() > 0):
        #     print(visit)
        #     while node.left:
        #         stack.enqueue_front(node.right)
        #         stack.enqueue_front(node.left)
        #         node = node.left
        #     else:
        #         node = stack.dequeue_front()
        #         if node not in visit:
        #             visit.append(node)
        #         check = stack.front()
        #         if (check.right is not None):
        #             #  check.right not in visit:
        #             if check.left:
        #                 stack.enqueue_front(stack.front().left)
        #             stack.enqueue_front(stack.front().right)
        # # # # # # # # # # # # #

        # Okay, last one
        # This wasn't meant to work

        # While it's not null
        # My usual "whiles" don't work
        # It was this, or make sure visit's len is same as the tree
        while True:
            # If the node is valid, grab right and left
            # Thanks Alan
            while node:
                if node.right:
                    stack.enqueue_front(node.right)
                stack.enqueue_front(node)
                node = node.left
            # If it's null, start dequeues
            else:
                node = stack.dequeue_front()
                # I don't even care at this point, just move the stack around
                # Originally, it would be left, parent, right;
                # needed left, right, node
                if node.right and node.right == stack.front():
                    stack.dequeue_front()
                    stack.enqueue_front(node)
                    node = node.right
                else:
                    # Put that in the visit. It's ALWAYS going to do this
                    # as a last case scenario
                    visit(node.data)
                    node = None

            if stack.length() == 0:
                break

            # print(stack.list, visit, "\n\n")

        return visit


    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: o(n)
        Memory usage: Based on size of level, so n/2? """
        #  Create queue to store nodes not yet traversed in level-order
        queue = deque()
        # Enqueue given starting node
        queue.append(start_node)
        # Loop until queue is empty
        while len(queue) > 0:
            # Dequeue node at front of queue
            node = queue.popleft()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left:
                queue.append(node.left)
            # Enqueue this node's right child, if it exists
            if node.right:
                queue.append(node.right)

    def __leaf_delete(self, node, parent):
        # If root, there's nothing left
        if self.root is node:
            self.root = None
        # Else, we just have parent link to nothing
        elif parent.right is node:
            parent.right = None
        elif parent.left is node:
            parent.left = None
        else:
            raise ValueError

    def __1branch_delete(self, node, parent):
        """Called by delete.
        Deletes node, replaces it with its single branch."""
        # If root, we need to get the descendent
        if self.root is node:
            if node.left is not None:
                self.root = node.left
            elif node.right is not None:
                self.root = node.right
            return
        # Else, we need to check the parent
        # It needs to grab the node's lone child
        elif parent.left == node:
            if node.right:
                parent.left = node.right
            elif node.left:
                parent.right = node.left
        elif parent.right == node:
            if node.right:
                parent.right = node.right
            elif node.left:
                parent.right = node.left
        else:
            raise ValueError

    def __2branch_delete(self, node, parent):
        """Called by delete.
        Deletes node, replaces with successor."""
        searchparent = node
        search = node.left
        while search.right is not None:
            searchparent = search
            search = search.right
        # Let's establish that we will ALWAYS go left,
        # Then all the way to the right
        print("SEARCH:", search)

        if search.is_1branch():
            # Only possibility for the node having a child is a left branch
            print("It's a one brancher")
            print(search, search.left, search.right)
            searchparent.right = search.left
            print(self.items_level_order(), "\n\n")

        # Moving on to the delete
        #
        if self.root is node:
            if search.is_leaf():
                # It can only be right anyway
                searchparent.right = None

            self.root = search

            if node.left is not search:
                search.left = node.left
            if node.right is not search:
                search.right = node.right
            return
        #
        elif parent.left == node:
            parent.left = search

            if node.left is not search:
                search.left = node.left
            if node.right is not search:
                search.right = node.right
        elif parent.right == node:
            parent.right = search
            if node.left is not search:
                search.left = node.left
            if node.right is not search:
                search.right = node.right

        else:
            raise ValueError

    def delete(self, item):
        """Oh man, this is a doozy."""
        if not self.contains(item):
            return
        parent = self._find_parent_node(item)
        node = self._find_node(item)
        node.is_1branch()

        if node.is_leaf():
            self.__leaf_delete(node, parent)
        elif node.is_1branch():
            self.__1branch_delete(node, parent)
        elif node.is_2branch():
            self.__2branch_delete(node, parent)
        self.size -= 1
        return

def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}, height: {}'.format(item, tree.size, tree.height()))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))

    # print("8:")
    # tree.delete(8)

    print(tree.items_level_order())
    print("\n1:")
    tree.delete(1)
    print(tree.items_level_order())
    print("\n2:")
    tree.delete(2)
    print(tree.items_level_order())
    # print("\n3:")
    # tree.delete(3)
    # print(tree.items_level_order())
    print("\n6:")
    tree.delete(6)
    print(tree.items_level_order())

    testtree = BinarySearchTree([7, 3, 1, 4, 2, 6, 5])
    print(testtree.items_level_order())
    testtree.delete(4)
    print(testtree.items_level_order())
    # Deleting root
    testtree.delete(7)
    print(testtree.items_level_order())
    testtree.delete(1)
    print(testtree.items_level_order())
    # Deleting root
    testtree.delete(3)
    print(testtree.items_level_order())

    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    tree = BinarySearchTree(items)
    print("====== DELETING 8 ====== ")
    tree.delete(8)
    print("====== DELETING 7 ====== ")

    print(tree.items_level_order())
    tree.delete(7)
    print(tree.items_level_order())

    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    tree = BinarySearchTree(items)
    print(tree._find_node(8))
    print(tree._find_node(4))
    print(tree._find_node(2))
    print(tree._find_node(1))

def test_AVL_tree():
    # items = [5, 4, 3, 2, 1]
    # tree = BinarySearchTree(items)
    # print(tree.items_level_order())
    # print(tree.items_in_order())

    items = [1, 4, 2, 3]
    tree = BinarySearchTree(items)
    print(tree.items_level_order())
    print(tree.items_in_order())
    # items = [1, 2, 3, 4, 5]
    # tree = BinarySearchTree(items)
    # print(tree.items_level_order())
    # print(tree.items_in_order())


if __name__ == '__main__':
    # test_binary_search_tree()
    test_AVL_tree()
