"""Сложность O(n)"""
def diameterOfBinaryTree(root):
    stack = [root]
    ans = 0
    while stack:
        node = stack.pop()
        if node.right:# Если есть правый элемент добавить в стак и найти максимумдля ответа
            stack.append(node.right)
            ans = max(ans, abs(node.right.val - node.val))
        if node.left:# Если есть левый элемент добавить в стак и найти максимумдля ответа
            stack.append(node.left)
            ans = max(ans, abs(node.left.val - node.val))
    return ans