class Queue:
    def __init__(self):
        self._items = []
        self._size = 0

    def enqueue(self, value):
        self._items.append(value)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self._size -= 1
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self):
        return 'Front -> ' + ' -> '.join(map(str, self._items)) + ' -> Rear'
