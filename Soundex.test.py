import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_multiple_characters(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Jefferson"), "J350")
        self.assertEqual(generate_soundex("Washington"), "W250")

    def test_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("123"), "1000")
        self.assertEqual(generate_soundex("Hello, World!"), "H400")

    def test_edge_cases(self):
        self.assertEqual(generate_soundex("AAAA"), "A000")
        self.assertEqual(generate_soundex("BBBB"), "B100")
        self.assertEqual(generate_soundex("CCCC"), "C200")

if __name__ == '__main__':
    unittest.main()
