"""O(n*log(n))"""
# geid - входные данные
grid = [[0, 0, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]
#Возможные перемещения
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# Высота и ширина матрицы
m, n = len(grid), len(grid[0])


def check_position(y, x):
    # Функция для проверки соседних ячеек
    if grid[y][x] == 0: # Если ячейка 0, то ничего не делать
        return
    grid[y][x] = 0 # иначе заменить 1 на 0
    for pos in moves:
        # Проверка закончился остров или нет
        new_r, new_c = y + pos[0], x + pos[1]
        if 0 <= new_r < m and 0 <= new_c < n: # Если есть куда двигаться запускаем рекурсию
            check_position(new_r, new_c)


def islands(grid):
    result = 0
    # Запускаем циклы для обхода крайних элементов матрицы
    for i in range(m):
        check_position(i, 0)
        check_position(i, n - 1)

    for j in range(n):
        check_position(0, j)
        check_position(m - 1, j)
    # Считаем оставшийся остров
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result += 1
    return result


print(islands(grid))
