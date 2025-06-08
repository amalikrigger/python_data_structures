class Stack:
    def __init__(self):
        self._items = []

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def push(self, x):
        self._items.append(x)

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


# s = Stack()
#
# print(s.size())
# s.push(1)
# s.push(2)
# s.pop()
# print(s.size())
# print(s.is_empty())
# s.pop()
# print(s.is_empty())
# s.push(3)
# s.push(4)
# s.push(5)
# print(s)
# print(s.is_empty())
# print(s.size())
# print(s.peek())
# s.pop()
# s.pop()
# s.pop()
# print(s.is_empty())   # True
# s.push(10)
# s.push(20)
# s.push(30)
# print(s)             # Top -> 30 -> 20 -> 10
# print(s.peek())      # 30
# print(s.pop())       # 30
# print(s)             # Top -> 20 -> 10
# print(s.size())      # 2
# print(s.is_empty())   # False
# print(s.pop())
# print(s.pop())
# print(s.peek())
# s.pop()






