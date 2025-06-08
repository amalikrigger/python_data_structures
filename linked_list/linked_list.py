from node import Node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def append(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = Node(value)
        self.__size += 1

    def prepend(self, value):
        if not self.__head:
            self.__head = Node(value)
        else:
            new_node = Node(value, self.__head)
            self.__head = new_node
        self.__size += 1

    def clear(self):
        self.__head = None
        self.__size = 0

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError('Index out of bounds')
        if not self.__head:
            self.prepend(value)
            return
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        current.next = Node(value, current.next)
        self.__size += 1

    def delete(self, value):
        if not self.__head:
            return
        if self.__head.value == value:
            self.__head = self.__head.next
            self.__size -= 1
            return
        current = self.__head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self.__size -= 1
                break
            current = current.next
        return

    def pop(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError('Index out of bounds')
        if index == 0:
            self.__head = self.__head.next
            self.__size -= 1
            return
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.__size -= 1

    def get(self, value):
        if not self.__head:
            return -1
        current = self.__head
        for i in range(self.__size):
            if current.value == value:
                return i
            current = current.next
        return -1

    def contains(self, value):
        if self.get(value) == -1:
            return False
        return True

    def length(self):
        return self.__size

    # def reverse(self):
    #     if not self.__head:
    #         return
    #     current = self.__head
    #     self.__head = Node(current.value)
    #     while current.next:
    #         temp = self.__head
    #         self.__head = Node(current.next.value, temp)
    #         current = current.next

    def reverse(self):
        current = self.__head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head = prev

    # def has_cycle(self):
    #     if not self.__head or not self.__head.next:
    #         return False
    #     slow = self.__head
    #     fast = self.__head.next
    #     while fast.next:
    #         if slow.value == fast.value:
    #             return True
    #         slow = slow.next
    #         fast = fast.next.next
    #     return False

    def has_cycle(self):
        fast = self.__head
        slow = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def print(self):
        current_node = self.__head
        elements = []
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(elements) + ' -> None'
