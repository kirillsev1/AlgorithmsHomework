"""Сложность O(n**2)"""
def averageOfLevels(self, root):
    q = [root] # Очередь
    ans = []
    while q:
        num, row = len(q), 0
        for i in range(num):# Запуск цикла по длине Очереди
            node = q.pop(0)# получаем текущий лист
            row += node.val# Прибавляем для счета ср. знач.
            if node.left:# Добавляем в список для перемещения влево и вправо
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(row / num)# Добавляем ср.знач. в ответ
    return ans