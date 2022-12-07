"""Сложность O(n) + O(n)"""


# Возьмем код из классной работы
def first_rob(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]


def rob(nums):
    if len(nums) == 1:
        return nums[0]
    # Запустим функцию 1 вора с элементами до последнего
    result1 = first_rob(nums[:len(nums) - 1])
    # запускаем функцию не учитывая 1 элемент
    result2 = first_rob(nums[1:])
    # Возвращаем максимум из результатов
    return max(result1, result2)


print(rob([1,2,3,1]))
