import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_names_with_similar_sounds(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")
    def test_names_with_h_w(self):
        self.assertEqual(generate_soundex("Hemming"), "H552")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_various_names(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_name_with_repeated_consonants(self):
        self.assertEqual(generate_soundex("Jackson"), "J250")
        self.assertEqual(generate_soundex("Tucker"), "T260")

if __name__ == '__main__':
    unittest.main()
