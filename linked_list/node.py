class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"Node({self.value})"











