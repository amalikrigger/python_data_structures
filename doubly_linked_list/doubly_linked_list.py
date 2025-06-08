from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def append(self, value):
        new_node = Node(value, None, self.__tail)
        if not self.__head:
            self.__head = new_node
            self.__tail = self.__head
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def prepend(self, value):
        new_node = Node(value, self.__head)
        if not self.__head:
            self.__head = new_node
            self.__tail = self.__head
        else:
            self.__head.prev = new_node
            self.__head = new_node
        self.__size += 1

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError('Index out of bounds')
        if not self.__head or index == 0:
            self.prepend(value)
            return
        if index == self.__size:
            self.append(value)
            return
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(value, current.next, current)
        current.next.prev = new_node
        current.next = new_node
        self.__size += 1

    def delete(self, value):
        if not self.__head:
            return
        if self.__head.value == value:
            self.pop()
            return
        if self.__tail.value == value:
            self.pop(self.__size - 1)
            return
        current = self.__head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                self.__size -= 1
                break
            current = current.next
        return

    def pop(self, index = 0):
        if index < 0 or index >= self.__size:
            raise IndexError('Index out of bounds')
        if index == 0:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size -= 1
            return
        current = self.__head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        if current.next:
            current.next.prev = current
        self.__size -= 1

    def get(self, value):
        if not self.__head:
            return -1
        if self.__head.value == value:
            return 0
        if self.__tail.value == value:
            return self.__size - 1
        current = self.__head
        if self.__head.value == value:
            return 0
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

    def print(self):
        current_node = self.__head
        elements = []
        while current_node:
            elements.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(elements) + ' -> None'
        # return 'None -> ' + ' -> '.join(elements) + ' -> None'


dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.insert(3, 6)
dll.insert(6, 7)
dll.insert(0, 8)
dll.delete(8)
dll.delete(6)
dll.delete(7)
dll.delete(75)
dll.pop()
dll.pop(2)
print(dll.get(3))
print(dll.print())


