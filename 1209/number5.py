"""Сложность O(n)"""
# Класс дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    ans = []
    stack = [(root, str(root.val))]

    while stack:# Пока есть листья
        node, result = stack.pop()# Получаем лист и его значение
        if node:# Если лист не пустой
            if node != root:# Если лист не первый добавляем ->
                result += '->' + str(node.val)
            if node.right:# Если есть правый элемент добавляем пердидущие значения со ->
                stack.append((node.right, result))
            if node.left:# Если есть левый элемент добавляем пердидущие значения со ->
                stack.append((node.left, result))
            if not node.right and not node.left:# Если нет след. листьев добавляем последовательность в ответx
                ans.append(result)
    return ans