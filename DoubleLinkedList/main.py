class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return f"Node({self.value})"


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def traverse(self):
        current_node = self.head

        while current_node:
            print(current_node.value, end=' ')
            current_node = current_node.next

    def reverse_traversal(self):
        cur = self.tail

        while cur:
            print(cur.value, end=' ')
            cur = cur.prev

    def search(self, target):
        cur = self.head
        # index = 0

        # while cur:
        #     if cur.value == target:
        #         return index
        #     cur = cur.next
        #     index += 1

        for i in range(self.length):
            if cur.value == target:
                return i
            cur = cur.next

        return False

    def get(self, index):
        if index < 0 or index >= self.length:
            return

        if index < self.length // 2:
            cur = self.head

            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail

            for _ in range(self.length - 1, index, -1):
                cur = cur.prev

        return cur

    def set_value(self, index, value):
        cur_node = self.get(index)

        if cur_node:
            cur_node.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("index out of bounds!")
            return

        if index == 0:
            self.prepend(value)
            return
        
        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        temp_node = self.get(index-1)

        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        if not self.head:
            return

        popped_node = self.head

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None

        self.length -= 1
        return popped_node

    def pop(self):
        popped_node = self.tail

        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None

        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
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
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)

            if temp_node.next is not None:
                result += " <-> "

            temp_node = temp_node.next

        return result


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(10)
    dll.append(1)
    dll.append(30)
    dll.append(15)
    dll.prepend(100)
    dll.prepend(123)

    # dll.set_value(0, 10000)

    # print(dll)
    # print(dll.search(0))

    # print(dll.get(6))

    print(dll)
    # dll.insert(-6, 1234)
    # dll.pop_first()
    # print(dll.pop())
    # print(dll.length)
    # print(dll)
    print(dll.remove(8))
    dll.delete_all()
    print(dll)
