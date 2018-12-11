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


LL = LinkedList()

for i in range(7):
    LL.add(i)

print(LL)
LL.reverse()
print(LL)
print(LL.head, LL.tail)
