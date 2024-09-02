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
    codes = [c for c in codes if c != '0' and c != codes[0]]
    soundex += ''.join(codes[:3])
    soundex = soundex.ljust(4, '0')
    return soundex
