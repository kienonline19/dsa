from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


lst = LinkedList()
print(lst)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


lst = LinkedList(10)

print(lst)
print(lst.head)
print(lst.tail)
print(lst.length)
print(lst.head.value)
print(lst.tail.value)
