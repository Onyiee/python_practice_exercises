def addition(number1: float, number2: float) -> float:
    result = number1 + number2
    return result


def multiplication(number1: float, number2: float) -> float:
    result = number1 * number2
    return result


def run_tests():
    assert addition(3, 3) == 6, "3 + 3 is 6"
    assert multiplication(3, 3) == 9, "3 * 3 is 9"
