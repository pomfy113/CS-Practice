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
        node = self.head
        prev = None
        self.tail = node

        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next

        self.head = prev

    def rotate(self, rotate):
        node = self.head

        for _ in range(rotate):
            prev = node
            node = node.next

        # Unchain
        prev.next = None
        self.tail = prev
        future_head = node

        while node.next is not None:
            node = node.next

        # Reattachment
        node.next = self.head
        self.head = future_head


LL = LinkedList()

for i in range(7):
    LL.add(i)

print(LL)
print("\n\n")

print("Reverse")
LL.reverse()
print(LL)
LL.reverse()
print("\n\n")

print("Rotating")
LL.rotate(3)
print(LL)
print("\n\n")

LL.rotate(4)
print(LL)
print("\n\n")
