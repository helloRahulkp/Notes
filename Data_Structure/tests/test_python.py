import unittest
from Python.AVLTree import AVLTree

class TestAVLTree(unittest.TestCase):
    def test_insert(self):
        tree = AVLTree()
        tree.insert(10)
        self.assertEqual(tree.root.value, 10)

if __name__ == "__main__":
    unittest.main()
