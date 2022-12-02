"""Сложность O(n)"""
# Класс дерева
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getDecimalValue(head: ListNode) -> int:
    # В ответ добавляем перывй элемент
    result = str(head.val)
    # Пока есть следующее значение в дереве к ответу прибавлять строковое значение и двигаться дальше
    while head.next:
        result += str(head.next.val)
        head = head.next
    # Вернуть ответ в десятиричной системе счистления
    return int(result, 2)

