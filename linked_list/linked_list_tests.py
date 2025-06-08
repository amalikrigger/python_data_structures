import unittest
from linked_list import LinkedList
from node import  Node

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_append(self):
        self.list.append(10)
        self.assertEqual(self.list.length(), 1)
        self.list.append(20)
        self.assertEqual(self.list.length(), 2)
        self.assertTrue(self.list.contains(20))

    def test_prepend(self):
        self.list.prepend(10)
        self.assertEqual(self.list.length(), 1)
        self.list.prepend(20)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(20), 0)

    def test_insert(self):
        self.list.append(1)
        self.list.append(3)
        self.list.insert(1, 2)
        self.assertEqual(self.list.get(2), 1)
        with self.assertRaises(IndexError):
            self.list.insert(10, 99)

    def test_delete(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.delete(2)
        self.assertFalse(self.list.contains(2))
        self.assertEqual(self.list.length(), 2)
        self.list.delete(1)
        self.assertFalse(self.list.contains(1))
        self.assertEqual(self.list.length(), 1)

    def test_pop(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.pop(1)
        self.assertFalse(self.list.contains(20))
        self.assertEqual(self.list.length(), 2)
        with self.assertRaises(IndexError):
            self.list.pop(5)

    def test_index_of(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.assertEqual(self.list.get('b'), 1)
        self.assertEqual(self.list.get('z'), -1)

    def test_contains(self):
        self.list.append(100)
        self.assertTrue(self.list.contains(100))
        self.assertFalse(self.list.contains(200))

    def test_length(self):
        self.assertEqual(self.list.length(), 0)
        self.list.append(1)
        self.list.append(2)
        self.assertEqual(self.list.length(), 2)

    def test_clear(self):
        self.list.append(1)
        self.list.append(2)
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
        self.assertFalse(self.list.contains(1))

    def test_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(self.list.get(3), 0)
        self.assertEqual(self.list.get(1), 2)

    def test_print_method(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.print(), '1 -> 2 -> 3 -> None')

    def test_print_empty_list(self):
        self.assertEqual(self.list.print(), ' -> None')

    def test_print_single_element(self):
        self.list.append('a')
        self.assertEqual(self.list.print(), 'a -> None')

    def test_print_after_delete(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.pop(1)
        self.assertEqual(self.list.print(), '1 -> 3 -> None')

    def test_print_after_clear(self):
        self.list.append(5)
        self.list.clear()
        self.assertEqual(self.list.print(), ' -> None')

    def test_print_after_reverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(self.list.print(), '3 -> 2 -> 1 -> None')

    def test_reverse_single_element(self):
        self.list.append('X')
        self.list.reverse()
        self.assertEqual(self.list.print(), 'X -> None')

    def test_reverse_empty_list(self):
        self.list.reverse()
        self.assertEqual(self.list.print(), ' -> None')

    def test_contains_on_empty_list(self):
        self.assertFalse(self.list.contains(10))

    def test_index_of_empty_list(self):
        self.assertEqual(self.list.get(100), -1)

    def test_multiple_deletes(self):
        self.list.append(10)
        self.list.append(20)
        self.list.append(30)
        self.list.delete(10)
        self.list.delete(30)
        self.assertEqual(self.list.print(), '20 -> None')

    def test_insert_at_zero_on_empty(self):
        self.list.insert(0, 'start')
        self.assertEqual(self.list.print(), 'start -> None')

    def test_insert_at_size_minus_one(self):
        self.list.append(1)
        self.list.append(2)
        self.list.insert(1, 1.5)
        self.assertEqual(self.list.print(), '1 -> 1.5 -> 2 -> None')

    def test_append_after_clear(self):
        self.list.append(1)
        self.list.clear()
        self.list.append(2)
        self.assertEqual(self.list.print(), '2 -> None')

    def test_prepend_after_clear(self):
        self.list.append(1)
        self.list.clear()
        self.list.prepend(0)
        self.assertEqual(self.list.print(), '0 -> None')

    def test_mixed_operations(self):
        self.list.prepend(3)
        self.list.append(4)
        self.list.insert(1, 'middle')
        self.list.delete(3)
        self.list.prepend('start')
        self.assertEqual(self.list.print(), 'start -> middle -> 4 -> None')

    def test_reverse_list(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.reverse()
        self.assertEqual(self.list.get(3), 0)
        self.assertEqual(self.list.get(1), 2)

    def test_reverse_list_two_elements(self):
        self.list.append(1)
        self.list.append(2)
        self.list.reverse()
        self.assertEqual(self.list.print(), '2 -> 1 -> None')

    def test_reverse_list_multiple_elements(self):
        for val in range(1, 6):  # Creates 1->2->3->4->5
            self.list.append(val)
        self.list.reverse()
        self.assertEqual(self.list.print(), '5 -> 4 -> 3 -> 2 -> 1 -> None')

    def test_reverse_list_single_element(self):
        self.list.append(42)
        self.list.reverse()
        self.assertEqual(self.list.print(), '42 -> None')

    def test_reverse_list_empty_list(self):
        self.list.reverse()
        self.assertEqual(self.list.print(), ' -> None')

    def test_reverse_list_twice_original_order(self):
        values = ['a', 'b', 'c', 'd']
        for val in values:
            self.list.append(val)
        self.list.reverse()
        self.list.reverse()
        self.assertEqual(self.list.print(), 'a -> b -> c -> d -> None')

    def test_has_cycle_empty_list(self):
        self.assertFalse(self.list.has_cycle())

    def test_has_cycle_single_node_no_cycle(self):
        self.list.append(1)
        self.assertFalse(self.list.has_cycle())

    def test_has_cycle_single_node_with_cycle(self):
        node = Node(1)
        node.next = node  # Creates a cycle
        self.list._LinkedList__head = node
        self.list._LinkedList__size = 1
        self.assertTrue(self.list.has_cycle())

    def test_has_cycle_multiple_nodes_no_cycle(self):
        for val in [1, 2, 3, 4]:
            self.list.append(val)
        self.assertFalse(self.list.has_cycle())

    def test_has_cycle_multiple_nodes_with_cycle(self):
        nodes = [Node(i) for i in range(5)]
        for i in range(4):
            nodes[i].next = nodes[i + 1]
        nodes[4].next = nodes[1]
        self.list._LinkedList__head = nodes[0]
        self.list._LinkedList__size = 5
        self.assertTrue(self.list.has_cycle())

if __name__ == '__main__':
    unittest.main()