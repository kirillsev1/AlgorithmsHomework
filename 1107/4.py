def maxScoreSightseeingPair(values):
    # Создаем переменную для ответа и поиска максимума
    max_num = 0
    ans = 0
    # Запускаем цикл по индексам values
    for i in range(1, len(values)):
        # сравниваем ans и каждое число списка values
        max_num = max(max_num - 1, values[i - 1] - 1)
        # Записываем максимум из ans и каждого элемента + максимальной разницы
        ans = max(ans, values[i] + max_num)
    # Возвращаем максимум
    return ans


print(maxScoreSightseeingPair([8, 1, 5, 2, 6]))
