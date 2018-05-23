
def two_sum(arr, S):
    sums = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j] == S):
                sums.append([arr[i], arr[j]])

    return sums


print(two_sum([3, 5, 2, -4, 8, 11], 7))
