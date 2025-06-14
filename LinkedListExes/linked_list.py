from random import randint


class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        cur = self.head

        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        values = [str(x.data) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        # result = 0

        # node = self.head

        # while node:
        #     result += 1
        #     node = node.next

        # return result
        return self.length

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return self.tail

    def generate(self, n, min_val, max_val):
        self.head = None
        self.tail = None

        for _ in range(n):
            self.add(randint(min_val, max_val))

        return self
    
    def remove_duplicates(self):
        if self.head is None:
            return
        
        seen = set()
        current = self.head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next

                if current == self.tail:
                    self.tail = prev

                self.length -= 1
            else:
                seen.add(current.data)
                prev = current
            current = current.next


if __name__ == "__main__":
    custom_ll = LinkedList()

    custom_ll.generate(10, 0, 99)

    custom_ll.add(100)
    custom_ll.add(10)
    custom_ll.add(100)

    print(custom_ll)
    print(len(custom_ll))

    custom_ll.remove_duplicates()

    print(custom_ll)
    print(len(custom_ll))
