class Pixel:
    def __init__(self, x=0, y=0, r=0, g=0, b=0):
        self._x = x
        self._y = y
        self._red = r
        self._green = g
        self._blue = b

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = self._green = self._blue = avg

    def print_pixel_info(self):
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print("X: {}, Y: {}, Color: ({}, {}, {}) Blue".format(self._x, self._y, self._red, self._green, self._blue))
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            print("X: {}, Y: {}, Color: ({}, {}, {}) Green".format(self._x, self._y, self._red, self._green, self._blue))
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            print("X: {}, Y: {}, Color: ({}, {}, {}) Red".format(self._x, self._y, self._red, self._green, self._blue))
        else:
            print("X: {}, Y: {}, Color: ({}, {}, {})".format(self._x, self._y, self._red, self._green, self._blue))


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()
