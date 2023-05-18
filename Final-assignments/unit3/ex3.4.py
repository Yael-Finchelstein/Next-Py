import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, i):
        self._char = char
        self._index = i

    def __str__(self):
        return 'The username contains an illegal character "{}" at index {}'.format(self._char, self._index)


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class MissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class MissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class MissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class MissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort
        elif len(username) > 16:
            raise UsernameTooLong
        check = True
        for char in username:
            c = char
            i = username.index(c)
            if char not in (string.ascii_letters + string.digits + '_'):
                check = False
                break
        if not check:
            raise UsernameContainsIllegalCharacter(c, i)

        if len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong
        if not any(c.isupper() for c in password):
            raise MissingUppercase
        elif not any(c.islower() for c in password):
            raise MissingLowercase
        elif not any(c.isdigit() for c in password):
            raise MissingDigit
        elif not any(c in string.punctuation for c in password):
            raise MissingSpecial

    except UsernameContainsIllegalCharacter as e:
        print(e)
        return True
    except UsernameTooShort as e:
        print(e)
        return True
    except UsernameTooLong as e:
        print(e)
        return True
    except PasswordMissingCharacter as e:
        print(e)
        return True
    except PasswordTooShort as e:
        print(e)
        return True
    except PasswordTooLong as e:
        print(e)
        return True

    else:
        print("OK")
        return False


def main():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    exception_raised = check_input(username, password)
    while exception_raised:
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        exception_raised = check_input(username, password)


if __name__ == '__main__':
    main()
