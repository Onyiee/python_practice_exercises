from Calculator import *


def run_tests():
    assert add(2, 3) == 5, "2 + 3 is 5"
    assert subtract(4, 2) == 2, "4 - 2 is 2"
    assert multiply(2, 3) == 6, "2 * 3 is 6"
    assert division(10, 5) == 2, "10 / 5 is 2"
    assert square_root(9) == 3, "3 * 3 is 9"
    assert square(2) == 4, "square of 2 is 4"


if __name__ == "__main__":
    run_tests()
