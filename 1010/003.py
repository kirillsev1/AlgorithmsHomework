"""Function which compares stones and jewels."""


def numJewelsInStones(jewels: str, stones: str) -> int:
    """Function counts jewels.

    Args:
        jewels: str - type of jewels.
        stones: str - type of stones.

    Returns:
        anser: int - number of jewels.
    """
    anser = 0
    # Проходим по камням
    for i in stones:
        # Проверяем является ли камень сокровищем
        if i in jewels:
            anser += 1
    return anser
print(numJewelsInStones('z', 'ZZ'))
