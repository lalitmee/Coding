from string import ascii_lowercase as asc_lower

def is_pangram(s):
    if (set(asc_lower) - set(s.lower()) == set([])):
        return True
    else:
        return False

is_pangram('The quick brown fox jumps over the lazy dog')
