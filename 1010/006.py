def getKth(lo, hi, k):
    steps = {}
    for i in range(lo, hi+1):
        steps[i] = 0

    for i in range(lo, hi+1):
        x = i
        step = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            step += 1
        steps[i] = step
    result = []
    for i, j in steps.items():
        result.append([i, j])
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i][1] > result[j][1]:
                result[i], result[j] = result[j], result[i]
    return result[k-1][0]


print(getKth(7, 11, 4))