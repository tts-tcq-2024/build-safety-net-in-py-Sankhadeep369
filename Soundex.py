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
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def generate_soundex(name):
    if not name:
        return ""

    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)
    soundex_length = 1  # Start with the first letter already included

    for char in name[1:]:
        code = get_soundex_code(char)

        if code == '0':
            continue  # Skip vowels and non-mapped characters

        if code != prev_code:  # Only add non-repeating codes
            soundex += code
            soundex_length += 1
            if soundex_length == 4:
                break

        prev_code = code

    return soundex.ljust(4, '0')  # Ensure the Soundex code is always 4 characters long

    # Pad with zeros if necessary to make length 4
    soundex = soundex.ljust(4, '0')

    return soundex
