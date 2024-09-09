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

# Refactored generate_soundex function with improved handling of adjacent consonants
def generate_soundex(name):
    if not name:
        return ""

    # First letter is directly appended
    soundex = name[0].upper()

    # Create a list of soundex codes using the lookup table
    codes = [get_soundex_code(c) for c in name[1:]]

    # Remove consecutive duplicate codes
    filtered_codes = []
    for i, code in enumerate(codes):
        if code != '0' and (i == 0 or code != filtered_codes[-1]):  # Avoid duplicates
            filtered_codes.append(code)

    # Build the final soundex code by combining the first letter and up to 3 additional codes
    soundex += ''.join(filtered_codes[:3])
    
    # Ensure the soundex code is 4 characters long, padding with zeros if necessary
    return soundex.ljust(4, '0')
