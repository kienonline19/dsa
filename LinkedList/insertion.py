class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        cur_node = self.head

        result = ''

        while cur_node is not None:
            result += str(cur_node.data)

            if cur_node.next is not None:
                result += ' -> '

            cur_node = cur_node.next

        return result

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError(f"{index} is an invalid index!")

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def traverse(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

    def search(self, value):
        # current = self.head

        # while current:
        #     if current.data == value:
        #         return True
        #     current = current.next

        # return False

        current, position = self.head, 0

        while current:
            if current.data == value:
                return (current, position)

            current = current.next
            position += 1

        return (None, -1)

    def get(self, index):
        if not self.head:
            raise IndexError("Cannot get from empty linked list!")

        if not isinstance(index, int):
            raise TypeError("Index must be an integer!")

        if index == -1:
            return self.tail

        if index < 0:
            index = self.length + index

        if index < 0 or index >= self.length:
            raise IndexError("Index out of range!")

        current = self.head

        for _ in range(index):
            current = current.next

        return current

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.data = value
            return True

        return False

    def pop_first(self):

        if self.head is None:
            raise TypeError("Empty Linked list!")

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return

        popped_node = self.tail

        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head

            while temp.next is not self.tail:
                temp = temp.next

            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < -1 or index >= self.length:
            return

        if index == 0:
            return self.pop_first()

        if index == self.length - 1 or index == -1:
            return self.pop()

        prev_node = self.get(index - 1)

        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


if __name__ == "__main__":
    sll = LinkedList()

    sll.append(10)
    sll.append(20)
    sll.append(30)

    sll.append(40)

    print(sll)

    sll.delete_all()
    print(sll)

