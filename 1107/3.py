def uniquePathsWithObstacles(obstacleGrid):
    # Создаем матрицу для ответа по размеру входных данных
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    # Первый элемент спика - робот = 1
    dp[0][0] = 1
    # Проход по всему списку
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            # Если встречаем камень
            if obstacleGrid[i][j] == 1:
                # Отмечаем в матрице камень
                dp[i][j] = 0
            else:
                # Если хоть один индекс больше 0
                if i > 0 or j > 0:
                    # То прибавляем и записываем кол-во путей в матрицу
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # Выводим последний элемент матрицы
    print(dp)
    return dp[-1][-1]


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
