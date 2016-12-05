import third
import unittest

class Test_third(unittest.TestCase):

    def test_letter_is_in_string(self):
        self.assertEqual(third.count_letter_in_string('ab', 'b'), 1)

    def test_letter_is_not_in_string(self):
        self.assertEqual(third.count_letter_in_string('ac', 'b'), 0)

    def test_not_string(self):
        self.assertEqual(third.count_letter_in_string(0, 'b'), 0)

if __name__ == '__main__':
    unittest.main()
