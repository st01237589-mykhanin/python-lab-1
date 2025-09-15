import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from generator_utils import even_odd_generator

class TestGenerator(unittest.TestCase):
    def test_even_odd_generator(self):
        gen = even_odd_generator()
        results = [next(gen) for _ in range(4)]
        self.assertEqual(results, ["Парне", "Непарне", "Парне", "Непарне"])

if __name__ == "__main__":
    unittest.main()