def fibonacci(n):
    """
    Принимает N уровень, до которого надо выполнить расчет.
    Возвращает list полученных чисел.
    """
    if n <= 0:
        return [0, ]

    sequence = [0, 1]

    if n == 1:
        return sequence

    for i in range(2, n + 1):
        next_num = sequence[-1] + sequence[-2]

        sequence.append(next_num)
    return sequence
