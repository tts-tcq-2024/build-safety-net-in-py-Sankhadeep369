# soundex.py

def get_soundex_code(char):
    """Get the soundex code for a single character."""
    char = char.upper()
    soundex_table = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return soundex_table.get(char, '0')

def is_vowel_or_special(char):
    """Check if a character is a vowel or a special character."""
    return char in 'AEIOUYHW'

def generate_soundex(name):
    """Generate the Soundex code for a given name."""
    if not name:
        return ""

    soundex = name[0].upper()  # Start with the first letter
    prev_code = get_soundex_code(soundex)
    codes = []

    for char in name[1:]:
        if is_vowel_or_special(char):
            continue
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            codes.append(code)
            prev_code = code

    # Join the soundex code and pad if necessary
    return (soundex + ''.join(codes)[:3]).ljust(4, '0')
