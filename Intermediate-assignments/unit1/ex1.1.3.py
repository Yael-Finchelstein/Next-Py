def is_divide_in_4(num):
    return num % 4 == 0


def four_dividers(number):
    return list(filter(is_divide_in_4, range(1, number + 1)))
