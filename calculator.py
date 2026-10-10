def addition(a: float, b: float) -> float:
    return a + b


def subtraction(a: float, b: float) -> float:
    return a - b


def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("На 0 делить нельзя")
    return a / b


def multiplication(a: float, b: float) -> float:
    return a * b


if __name__ == "__main__":
    a = 2
    b = 3

    print(addition(a, b))
    print(subtraction(a, b))
    print(division(a, b))
    print(multiplication(a, b))

    b = 0
    print(division(a, b))