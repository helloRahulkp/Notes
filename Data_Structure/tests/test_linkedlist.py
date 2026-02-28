import unittest
from Python.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.head.next.value, 2)

if __name__ == "__main__":
    unittest.main()
