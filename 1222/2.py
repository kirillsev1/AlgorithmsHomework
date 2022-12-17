"""O(n)"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(node, low, high):
    if not node: # Если узел пустой вернуть None
        return None
    if node.val < low:# Если значение узла меньше маленького таргета, то нет смысла идти влево
        return trimBST(node.right, low, high)
    elif node.val > high:# Если значение узла больше второго таргета, то нет смысла идти вправо
        return trimBST(node.left, low, high)
    else:# В остальных случаях надо идти и влево и вправо
        node.left = trimBST(node.left, low, high)
        node.right = trimBST(node.right, low, high)
        return node
    return trimBST(node, low, high)
