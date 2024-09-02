import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_multiple_adjacent_duplicates(self):
        self.assertEqual(generate_soundex("hello"), "H400")

    def test_duplicates_separated_by_vowel(self):
        self.assertEqual(generate_soundex("example"), "E236")

    def test_duplicates_separated_by_consonant(self):
        self.assertEqual(generate_soundex("winter"), "W543")

    def test_long_name(self):
        self.assertEqual(generate_soundex("abcdefghijklmnopqrstuvwxyz"), "A23456")

    
if __name__ == '__main__':
    unittest.main()
