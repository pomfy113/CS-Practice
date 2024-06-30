
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
            # First, set up temporary variable
            next = node.next
            # Made the current node connect to the previous
            node.next = prev
            # Make this current node the "previous"
            prev = node
            # move to the next one
            node = next
        
        self.head = prev
    
    def rotate(self, rotates):
        node = self.head
        prev = None
        for _ in range(rotates):
            prev = node 
            node = node.next
        prev.next = None
        self.tail = prev
        new_head = node

        while node.next is not None:
            node = node.next

        node.next = self.head
        self.head = new_head


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
# print("\n\n")

# LL.rotate(4)
# print(LL)
# print("\n\n")
