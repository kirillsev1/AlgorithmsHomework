import random
def findKthLargest(nums, k):
    if not nums:
        return
    ran = random.choice(nums)
    left = [x for x in nums if x > ran]
    mid = [x for x in nums if x == ran]
    right = [x for x in nums if x < ran]
    L, M = len(left), len(mid)
    if k <= L:
        return findKthLargest(left, k)
    elif k > L + M:
        return findKthLargest(right, k - L - M)
    else:
        return mid[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
