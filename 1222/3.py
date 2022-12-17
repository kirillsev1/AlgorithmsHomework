"""O(len(word1) * len(word2))"""
def out(arr):
    for i in arr:
        print(i)
def minDistance(word1, word2):
    w1 = len(word1)
    w2 = len(word2)
    dp = [[0 for _ in range(w2 + 1)] for _ in range(w1 + 1)]# Создаем матрицу по размерам слов
    for i in range(w1 + 1):
        for j in range(w2 + 1):# Циклы по размерам слов
            if i == 0 and j == 0:# порграмма на первом элементе матрицы он равен 0
                dp[i][j] = 0
            elif i == 0:# Если j > 0, то смотрим на преидущий элемент, т.к. там записано кол-во шагов для преобразования одной буквы в другую
                dp[i][j] = dp[i][j - 1] + 1# Делаем 1 операцию
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + 1
            elif word1[i - 1] == word2[j - 1]:# Если буквы совпадают то сохраняем кол-во операций
                # print(i, j)
                dp[i][j] = dp[i - 1][j - 1]
            else:
                print(i, j)
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1# Если программа не на первой строке и не в первом столбце и буквы не совпадают,
                # то берем минимальное кол-во преобразований и делаем одну операцию
    out(dp)
    return dp[w1][w2]

print(minDistance('sea', 'tea'))