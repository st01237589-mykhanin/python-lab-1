import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from io import StringIO
from unittest.mock import patch
from string_utils import print_string, check_case, word_to_upper_list

class TestStringUtils(unittest.TestCase):
    def test_print_string(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_string("Print String")
            self.assertEqual(fake_out.getvalue().strip(), "Print String")

    def test_print_string_invalid_type(self):
        with self.assertRaises(TypeError):
            print_string(1)

    def test_check_case_upper(self):
        self.assertEqual(check_case("CHECK CASE"), "Усі літери великі")

    def test_check_case_lower(self):
        self.assertEqual(check_case("check case"), "Усі літери малі")

    def test_check_case_mixed(self):
        self.assertEqual(check_case("cHeCk CaSe"), "Літери змішані")

    def test_check_case_empty(self):
        self.assertEqual(check_case(""), "Порожній рядок")

    def test_check_case_invalid_type(self):
        with self.assertRaises(TypeError):
            check_case(1)

    def test_word_to_upper_list(self):
        self.assertEqual(word_to_upper_list("smogtether"), ['S', 'M', 'O', 'G', 'T', 'E', 'T', 'H', 'E', 'R'])

    def test_word_to_upper_list_invalid_type(self):
        with self.assertRaises(TypeError):
            word_to_upper_list(1)

if __name__ == "__main__":
    unittest.main()