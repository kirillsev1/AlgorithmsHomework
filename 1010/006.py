def getKth(lo, hi, k):
    # O(n) + O(n) + O(n**2)
    # Создаем словарь с числами от lo до hi
    steps = {}
    for i in range(lo, hi+1):
        steps[i] = 0

    # Обходим каждое число
    for i in range(lo, hi+1):
        x = i
        step = 0
        # Преобразовываем число к 1 и считаем кол-во действий
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            step += 1
        steps[i] = step
    result = []
    # Записываем все значения для сортировки
    for i, j in steps.items():
        result.append([i, j])
    # Сортируем все элементы по второму значеню списков
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i][1] > result[j][1]:
                result[i], result[j] = result[j], result[i]
    # Возвращаем -k элемент, т.к. сортировка от большего к меньшему
    return result[k-1][0]


print(getKth(7, 11, 4))