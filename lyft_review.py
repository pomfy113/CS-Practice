class Node:
    def __init__(self, number):
        self.data = number
        self.next = None

    def __repr__(self):
        return '[Node - {}]'.format(self.data)

class LinkedList:
    def __init__(self):
        self.root = None
        self.tail = None

    def __repr__(self):
        node = self.root
        list = ""
        while node is not None:
            list += " {} ".format(node)
            node = node.next

        return list

    def add(self, num):
        node = Node(num)

        if self.root is None:
            self.root = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node



LL = LinkedList()

for i in range(7):
    LL.add(i)

print(LL)
