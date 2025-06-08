class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return False

class LinkedListStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def push(self, value):
        new_node = Node(value, self._top)
        self._top = new_node
        self._size += 1

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._top.value

    def is_empty(self):
        return self._top is None

    def size(self):
        return self._size

    def clear(self):
        self._top = None
        self._size = 0

    def to_list(self):
        current_node = self._top
        items = []
        while current_node is not None:
            items.append(current_node.value)
            current_node = current_node.next
        return items

    def __str__(self):
        current = self._top
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return 'Top -> ' + ' -> '.join(items) + ' -> None'

    def __len__(self):
        return self._size

    def __bool__(self):
        return not self.is_empty()
