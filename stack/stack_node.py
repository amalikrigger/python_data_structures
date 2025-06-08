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

class StackNode:
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.value

    def push(self, x):
        new_node = Node(x, self.top)
        self.top = new_node
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size

    def clear(self):
        self.top = None

    def to_list(self):
        current_node = self.top
        items = []
        while current_node is not None:
            items.append(current_node.value)
            current_node = current_node.next
        return items

    def __str__(self):
        current_node = self.top
        items = []
        while current_node is not None:
            items.append(str(current_node.value))
            current_node = current_node.next
        return ', '.join(items)

    def __len__(self):
        return self.size

    def __bool__(self):
        return not self.is_empty()


stack = StackNode()

stack.push(6)
stack.push(7)
stack.push(8)
stack.push(10)
stack.push(25)
stack.push(50)
print(str(stack.size))
print(stack)
print(stack.peek())
print(stack.pop())
print(stack)
print(str(stack.size))
print(stack.pop())
print(str(stack.size))
stack.clear()
print(str(stack.is_empty()))

