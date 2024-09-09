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

    # Create a list of soundex codes using the lookup table and skip invalid characters
    codes = [get_soundex_code(c) for c in name[1:] if get_soundex_code(c) != '0']

    # Remove consecutive duplicates (this includes 'hw' rules automatically)
    filtered_codes = [codes[0]] if codes else []
    for i in range(1, len(codes)):
        if codes[i] != codes[i - 1]:
            filtered_codes.append(codes[i])

    # Build final soundex code
    soundex += ''.join(filtered_codes[:3])
    
    # Ensure the soundex code is 4 characters long, padding with zeros if necessary
    return soundex.ljust(4, '0')
