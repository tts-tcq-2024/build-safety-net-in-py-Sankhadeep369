import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    def test_same_sound_code(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")

    def test_different_first_letter(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")

    def test_various_names(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("Honeyman"), "H555")

    def test_names_with_h_w(self):
        self.assertEqual(generate_soundex("Hemming"), "H552")
        self.assertEqual(generate_soundex("Hemmingway"), "H552")

    def test_zero_padding(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("Ab"), "A100")
        self.assertEqual(generate_soundex("Abc"), "A120")

if __name__ == '__main__':
    unittest.main()
