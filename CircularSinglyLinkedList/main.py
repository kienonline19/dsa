class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

    def __str__(self):
        temp_node = self.head

        result = ""

        while temp_node is not None:
            result += str(temp_node.data)
            temp_node = temp_node.next

            if temp_node == self.head:
                break

            result += " -> "

        return result

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.length += 1

    def insert(self, index, value):
        if index > self.length or index < 0:
            raise IndexError("Index out of range")

        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

            if current == self.head:
                break

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

            if current == self.head:
                break

        return False

    def get(self, index):
        if self.length == 0 or index < -1 or index >= self.length:
            return

        if index == -1:
            return self.tail

        current = self.head

        for _ in range(index):
            current = current.next

        return current

    def set_value(self, index, value):
        cur_node = self.get(index)

        if cur_node:
            cur_node.data = value
            return True

        return False

    def pop_first(self):
        if self.length == 0:
            return

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head

            while temp.next is not self.tail:
                temp = temp.next

            temp.next = self.head
            self.tail = temp

        popped_node.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return

        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()

        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.length == 0:
            return

        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1


if __name__ == "__main__":
    csll = CSLinkedList()
    csll.append(1)
    csll.append(10)
    csll.append(100)

    csll.prepend(50)
    csll.insert(2, 123)
    # csll.insert(10, 145)

    # print(csll)
    # print(csll.tail.data)
    # print(csll)
    # csll.traverse()

    # is_ok = csll.search(10)

    # if is_ok:
    #     print("Found")
    # else:
    #     print("Not found")

    # print(csll.get(-10))

    # csll.set_value(2, 1000)

    # print(csll)
    # print(csll.pop())

    # print(csll)
    # print(csll)
    # print(csll.remove(4))
    # print(csll)
    # print(csll.tail)
    csll.delete_all()
    print(csll)
    print(csll)
