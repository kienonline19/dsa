class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.value})"
    

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self, val):
    #     new_node = Node(val)
    #     self.head = new_node
    #     self.tail = new_node
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.head.prev = new_node
            self.tail.next = new_node

            new_node.prev = self.tail
            new_node.next = self.head

            self.head = new_node

        self.length += 1

    def traverse(self):
        current = self.head

        while True:
            print(current.value)
            current = current.next

            if current is self.head:
                break

    def reverse_traverse(self):
        current_node = self.tail

        while current_node:
            print(current_node.value)
            current_node = current_node.prev

            if current_node is self.tail:
                break

    def search(self, target):
        current = self.head

        while current:
            if current.value == target:
                return True
            
            current = current.next

            if current is self.head:
                break

        return False
    
    def get(self, index):
        current_node = None

        if index < 0 or index >= self.length:
            return current_node

        if index < self.length // 2:
            current_node = self.head

            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail

            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds")
            return
        
        if index == 0:
            self.prepend(value)
        elif index >= self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)

            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
            self.length += 1

    def pop_first(self):
        if self.length == 0:
            return

        popped_node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

            popped_node.next = None
            popped_node.prev = None

            self.head.prev = self.tail
            self.tail.next = self.head

        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 0:
            return

        popped_node = self.tail

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev

            popped_node.next = None
            popped_node.prev = None

            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -= 1
        return popped_node
    
    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False

    def remove(self, index):
        if self.length == 0:
            return

        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()

        popped_node = self.get(index)

        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev

        popped_node.next = None
        popped_node.prev = None

        self.length -= 1

        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ''

        while current:
            result += str(current.value)

            if current.next is self.head:
                break
            result += " <-> "
            current = current.next

        return result


if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    cdll.append(10)

    cdll.append(20)
    cdll.prepend(12)

    cdll.prepend(123)
    # print(cdll.tail.value)
    # print(cdll.tail.next.value)
    # print(cdll.head.prev.value)
    # print(cdll.length)

    print(cdll)
    # cdll.traverse()
    # cdll.reverse_traverse()

    # print(cdll.search(101))
    # print(cdll.get(4))

    # print('-' * 20)

    # print(cdll.set_value(1, 100))

    # print(cdll)

    # cdll.insert(-1, 234)

    # cdll.pop_first()

    # print(cdll.remove(3))
    cdll.delete_all()
    print(cdll)
    print(cdll.length)
