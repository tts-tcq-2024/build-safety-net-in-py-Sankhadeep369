def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')

def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()
    codes = [get_soundex_code(c) for c in name[1:]]
    codes = [c for c in codes if c != '0']

    # Create a copy of the codes list to avoid modifying the original
    codes_copy = codes[:]

    # Handle duplicates
    for i in range(len(codes_copy) - 2):
        if (codes_copy[i] == codes_copy[i + 2] and  # Check i and i+2 for duplicates
                (codes_copy[i + 1] in 'AEIOU' or  # Check if i+1 is a vowel
                 (codes_copy[i + 1] in ('H', 'W') and i + 2 < len(codes_copy) and codes_copy[i + 3] in 'AEIOU'))):  # Check for 'H' or 'W' followed by vowel
            del codes_copy[i + 1]

    soundex += ''.join(codes_copy[:3])
    soundex = soundex.ljust(4, '0')
    return soundex
