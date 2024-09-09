def get_soundex_code(c):
    c = c.upper()
    lookup_table = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return lookup_table.get(c, '0')

def generate_soundex(name):
    if not name:
        return ""

    # First letter is directly appended
    soundex = name[0].upper()

    # Create a list of soundex codes using the lookup table, ignoring vowels and 'h', 'w'
    codes = []
    prev_code = get_soundex_code(soundex)  # Start with the first letter's soundex code

    for char in name[1:]:
        code = get_soundex_code(char)
        # Skip if the code is '0' (vowels, h, w) or if it's the same as the previous code
        if code != '0' and code != prev_code:
            codes.append(code)
            prev_code = code

    # Build the final soundex code by combining the first letter and up to 3 additional codes
    soundex += ''.join(codes[:3])
    
    # Ensure the soundex code is 4 characters long, padding with zeros if necessary
    return soundex.ljust(4, '0')
