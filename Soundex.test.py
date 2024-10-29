# test_soundex.py

import unittest
from soundex import generate_soundex, get_soundex_code

class TestSoundex(unittest.TestCase):

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('H'), '0')
        self.assertEqual(get_soundex_code('W'), '0')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code(''), '0')

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex(''), '')
        self.assertEqual(generate_soundex('Robert'), 'R163')
        self.assertEqual(generate_soundex('Rupert'), 'R163')
        self.assertEqual(generate_soundex('Rubin'), 'R150')
        self.assertEqual(generate_soundex('Ashcraft'), 'A261')
        self.assertEqual(generate_soundex('Smith'), 'S530')
        self.assertEqual(generate_soundex('Johnson'), 'J525')
        self.assertEqual(generate_soundex('Honeyman'), 'H500')
        self.assertEqual(generate_soundex('Jackson'), 'J500')
        self.assertEqual(generate_soundex('T'), 'T000')
        self.assertEqual(generate_soundex('A'), 'A000')
        self.assertEqual(generate_soundex('Al'), 'A400')
        self.assertEqual(generate_soundex('Ali'), 'A400')

    def test_special_characters_and_vowels(self):
        # Test sequences with consecutive h and w
        self.assertEqual(generate_soundex('Ashworth'), 'A263')
        self.assertEqual(generate_soundex('Tolhwest'), 'T430')
        # Test cases with multiple vowels and no consonants
        self.assertEqual(generate_soundex('AEOU'), 'A000')
        self.assertEqual(generate_soundex('AEIOUY'), 'A000')
        # Test case where letters map to the same code and are separated by h or w
        self.assertEqual(generate_soundex('Bhbh'), 'B100')

if __name__ == '__main__':
    unittest.main()
