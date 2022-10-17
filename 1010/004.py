"""Function which remake array"""


def minimumAbsDifference(arr):
    # O(n*log(n)) + O(n) + O(n)
    # Стандартная сортировка
    arr.sort()
    # Создаем список для пар, огромное число для замены и словать
    pair = []
    diff = 10000000
    dct = {}
    # Запускаем цикл по длине списка для поиска минимальной разницы
    for i in range(len(arr) - 1):
        # Записываем в diff  значение diff или мождуль разницы двух чисел
        diff = min(diff, abs(arr[i] - arr[i + 1]))
        # Если наше число в Словаре
        if arr[i] in dct:
            # Прибавить к value 1
            dct[arr[i]] += 1
        else:
            # Иначе обнулить значение value до 1
            dct[arr[i]] = 1
    # Если число в словаре
    if arr[-1] in dct:
        # Прибавить к value 1
        dct[arr[-1]] += 1
    else:
        # Иначе обнулить значение value до 1
        dct[arr[-1]] = 1
    # Запускаем цикл по длине
    for i in range(len(arr)):
        # Если сило + разница в словаре
        if arr[i] + diff in dct:
            # Добавим пары
            pair.append([arr[i], arr[i] + diff])
    # Возвращаем список пар
    return pair

print(minimumAbsDifference([4, 3, 2, 1,]))