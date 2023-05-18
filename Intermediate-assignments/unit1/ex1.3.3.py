def is_funny(string):
    return not any(char != 'a' and char != 'h' for char in string)
