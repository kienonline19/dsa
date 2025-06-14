class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"Node({self.value})"


if __name__ == "__main__":
    new_node = Node(10)
    print(new_node)
