def shift_chars_backward(password):
    shifted_password = ""
    for char in password:
        if char.islower():
            shifted_char = chr(ord(char) - 2)
            if shifted_char < 'a':
                shifted_char = chr(ord(shifted_char) + 26)
            shifted_password += shifted_char
        else:
            shifted_password += char
    return shifted_password


def shift_chars_backward_one_liner(password):
    return ''.join([chr(ord(char)-2) if char.islower() else char for char in password]).replace("_", "y").replace("`", "z")


password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(shift_chars_backward_one_liner(password))
print(shift_chars_backward(password))
