def throw_stop_iteration():
    y = []
    x = iter(y)
    print(x.__next__())


def throw_zero_division_error():
    num = 0
    result = 1 / num


def throw_assertion_error():
    assert False, "AssertionError exception"


# def throw_import_error():
#     from crypt import pwd


def throw_key_error():
    my_dict = {"key": "value"}
    value = my_dict["non_existing_key"]


# def throw_syntax_error():
#     x = y = 0
#     if x == y
#         print("True")

# def throw_indentation_error():
#     if True:
#     print("IndentationError exception")


def throw_type_error():
    x = "10"
    y = 5
    z = x + y


def main():

    throw_stop_iteration()
    throw_zero_division_error()
    throw_assertion_error()
    # throw_import_error()
    throw_key_error()
    # throw_syntax_error()
    # throw_indentation_error()
    throw_type_error()


if __name__ == "__main__":
    main()
