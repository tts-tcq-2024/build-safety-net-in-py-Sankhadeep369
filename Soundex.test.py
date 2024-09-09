import unittest

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_names_with_h_w(self):
        self.assertEqual(generate_soundex("Hemming"), "H552")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")

    def test_various_names(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")  # Should now pass
        self.assertEqual(generate_soundex("Pfister"), "P236")

if __name__ == '__main__':
    unittest.main()
