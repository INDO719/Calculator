"""
calculator.py

Программа-калькулятор с функциями сложения, вычитания, умножения и деления

Основные возможности:
- Сложение двух чисел
- Вычитание из одного числа другого
- Деление одного числа на другое
- Умножение двух чисел

Дата создания: 2026-10-09
"""


def addition(a: float, b: float) -> float:
    """
    Складывает два числа

    Args:
        a (float): Первое число
        b (float): Второе число
    
    Returns:
        float: Сумма первого и второго числа
    
    Example:
        >>> addition(2, 3)
        5
    """
    return a + b


def subtraction(a: float, b: float) -> float:
    """
    Вычитает одно число из другого

    Args:
        a (float): Первое число
        b (float): Второе число
    
    Returns:
        float: Разница первого и второго числа
    
    Example:
        >>> addisubtractiontion(5, 3)
        2
    """
    return a - b


def division(a: float, b: float) -> float:
    """
    Делит одно число на другое

    Args:
        a (float): Первое число
        b (float): Второе число
    
    Returns:
        float: Частное первого на второе число
    
    Raises:
        ValueError: Если число b равно 0

    Example:
        >>> division(6, 3)
        2
    """
    if b == 0:
        raise ValueError("На 0 делить нельзя")
    return a / b


def multiplication(a: float, b: float) -> float:
    """
    Умножает два числа

    Args:
        a (float): Первое число
        b (float): Второе число
    
    Returns:
        float: Произведение первого и второго числа
    
    Example:
        >>> multiplication(2, 3)
        6
    """
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