# soundex.py

def get_soundex_code(char):
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
    return char in 'AEIOUYHW'

def process_character(char, prev_code):
    code = get_soundex_code(char)
    if code != '0' and code != prev_code:
        return code
    return None

def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    codes = [
        process_character(char, prev_code)
        for char in name[1:]
        if not is_vowel_or_special(char)
    ]
    # Filter out None values and get up to 3 codes
    filtered_codes = list(filter(None, codes))[:3]

    # Append the first letter and three digits or pad with '0'
    return (soundex + ''.join(filtered_codes)).ljust(4, '0')
