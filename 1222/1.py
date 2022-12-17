"""O(n*log(n))"""
def findLongestChain(pairs):
    new_pairs = sorted(pairs, key=lambda k: k[1])#Сортируем по вторым элементам списков
    cnt = 0 # Инициализируем счетчик и переменную для записи чисел
    num = 0
    for i in new_pairs:#Обход по парам
        left, right = i
        if num < left:# Если настоящее число меньше левого
            num = right# Настоящее число становиться правым и счетчик увеличиваем
            cnt += 1
    return cnt


print(findLongestChain([[1, 2], [2, 3], [3, 4]]))
