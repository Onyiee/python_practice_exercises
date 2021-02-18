def add(num1: float, num2: float) -> float:
    """ A function that adds two numbers"""
    # logic here
    num3 = num1 + num2
    return num3


print(add(1, 2))


def subtract(num1: float, num2: float) -> float:
    """ A function that subtracts two numbers"""
    # logic here
    num3 = num1 - num2
    return num3


print(subtract(1, 2))


def multiply(num1: float, num2: float) -> float:
    """ A function that multiplies two numbers"""
    # logic here
    num3 = num1 * num2
    return num3


print(multiply(5, 10))


def division(num1: float, num2: float) -> float:
    """ A function that divides two numbers"""
    # logic here
    num3 = num1 / num2
    return num3


print(division(9, 3))


def square_root(num1: float) -> float:
    """ A function that returns the square root of a number"""
    # logic here
    num2 = num1 ** 0.5
    return num2


print(square_root(9))


def square(num1: float) -> float:
    """ A function that returns the square  of a number"""
    # logic here
    num2 = num1 ** 2
    return num2


print(square(5))


def main():
    # run all the tests
    # add two numbers
    x = 2
    y = 10
    z = add(x, y)
    print(f"x + y: {x} + {y} = {z}")


if __name__ == "__main__":
    main()
