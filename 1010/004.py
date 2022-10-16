"""Function which remake array"""


def minimumAbsDifference(arr):
    arr.sort()
    pair = []
    diff = float("inf")
    dct = {}
    for i in range(len(arr) - 1):
        diff = min(diff, abs(arr[i] - arr[i + 1]))
        if arr[i] in dct:
            dct[arr[i]] += 1
        else:
            dct[arr[i]] = 1
    if arr[-1] in dct:
        dct[arr[-1]] += 1
    else:
        dct[arr[-1]] = 1
    for i in range(len(arr)):
        if arr[i] + diff in dct:
            pair.append([arr[i], arr[i] + diff])
    return pair

print(minimumAbsDifference([4, 3, 2, 1,]))