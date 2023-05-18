import functools


def add(x, y):
    return x + y


def sum_of_digits(number):
    return functools.reduce(add, map(int, str(number)))
