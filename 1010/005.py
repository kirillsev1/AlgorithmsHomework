import random
def findKthLargest(nums, k):
    # O(n) + O(n) + O(n)
    # Проверяем пустое nums или нет
    if not nums:
        return
    # Выбираем случайным образом элемент
    ran = random.choice(nums)
    # Собираем список из чисел, которе меньше ran
    left = [x for x in nums if x > ran]
    # Собираем список из чисел, которе равны ran
    mid = [x for x in nums if x == ran]
    # Собираем список из чисел, которе юольше ran
    right = [x for x in nums if x < ran]
    # Сохраняем длинну списков lift и mid
    L, M = len(left), len(mid)
    # Если L меньше k
    if k <= L:
        # Запускаем рекурсию с таким же k
        return findKthLargest(left, k)
    elif k > L + M:
        # Запускаем рекурсию с k меньшим, чем L + m
        return findKthLargest(right, k - L - M)
    else:
        # Возвращем центральное значение
        return mid[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
