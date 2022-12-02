grid = [[0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]]
m, n = len(grid), len(grid[0])
ans = 0


def solve(i, j):# Функция которая заменяет каждую ячейку на 1 для определения где функция уже побывала
    grid[i][j] = 1# Если существует соседняя ячейка то запускаем рекурсию
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= i + x < m and 0 <= j + y < n and grid[i+x][j+y] == 0:
            solve(i+x, j+y)


# Запуск функцмм поиска для каждого 0 в матрице
for i in range(m):
    if grid[i][0] == 0:
        solve(i, 0)
    if grid[i][n-1] == 0:
        solve(i, n-1)
# Запуск функцмм поиска для каждого 0 в матрице
for j in range(n):
    if grid[0][j] == 0:
        solve(0, j)
    if grid[m-1][j] == 0:
        solve(m-1, j)
# Обход всех оставшихся ячеек и записываем в ответ
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            ans += 1
            solve(i, j)
print(ans)
