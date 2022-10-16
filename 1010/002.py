"""Function which counts number of matches."""


def numberOfMatches(n):
    """Function counts number of matches by division on 2.

    Args:
        n: int - number of teams.

    Returns:
        match: int - number of matches between teams.
    """
    # O(n)
    match = 0
    # Если одна команда, возвращаем 0
    if n == 1:
        return 0
    # Пока больше 1 команды
    while n > 1:
        # Проверка на четность кол-ва команд
        if n % 2 == 0:
            # Сокращаем кол-во команд + добавляем кол-во матчей
            n //= 2
            match += n
        else:
            # Если не четное кол-во команд, 1 проходит дальше
            match += (n - 1) // 2
            n = ((n - 1) // 2) + 1
    return match

print(numberOfMatches(7))