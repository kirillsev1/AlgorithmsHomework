"""Reduce a number to zero."""


def numberofsteps(num: int) -> int:
    """Find number of steps.

    Args:
        num: int - first number.

    Returns:
        steps: int - number of steps
    """
    # n(log(n))
    steps = 0
    # Цикл пока число не равно 0
    while num != 0:
        # Проверка на четнось
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        # Счет шагов
        steps += 1
    return steps


print(numberofsteps(8))
