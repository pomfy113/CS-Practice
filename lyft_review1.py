"""Going to go with basic linked list stuff here."""

class Node:
    def __init__(self, number):
        self.data = number
        self.next = None

    def __repr__(self):
        return '[Node - {}]'.format(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        node = self.head
        list = ""
        while node is not None:
            list += " {} ".format(node)
            node = node.next

        return list

    def add(self, num):
        node = Node(num)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def reverse(self):
        curr = self.head
        prev = None
        self.tail = curr

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def rotate(self, rotate):
        node = self.head
        prev = None

        for _ in range(rotate):
            prev = node
            node = node.next

        # Unchain
        prev.next = None
        self.tail = prev

        # Keep track of future head
        future_head = node

        while node.next is not None:
            node = node.next

        # Reassignment
        node.next = self.head
        self.head = future_head

LL = LinkedList()

for i in range(7):
    LL.add(i)

print(LL)
print("\n\n")

LL.reverse()
print(LL)
print(LL.head, LL.tail)
LL.reverse()
print("\n\n")

LL.rotate(3)
print(LL)
print("\n\n")

LL.rotate(4)
print(LL)
print("\n\n")
