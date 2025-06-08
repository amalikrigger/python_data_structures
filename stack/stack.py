class Stack:
    def __init__(self):
        self._items = []

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def push(self, value):
        self._items.append(value)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()

    def to_list(self):
        return list(reversed(self._items))

    def __str__(self):
        return 'Top -> ' + ' -> '.join(map(str, reversed(self._items)))

    def __len__(self):
        return self.size()

    def __bool__(self):
        return not self.is_empty()




