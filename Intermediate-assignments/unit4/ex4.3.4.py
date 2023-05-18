def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
