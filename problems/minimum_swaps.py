a = [7, 1, 3, 2, 4, 5, 6]
b = [1, 3, 5, 2, 4, 6, 7]


def minimun_swaps(a):
    swaps = 0
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) -1 -i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1

    return swaps


print('Should be 5 and returned: ' + str(minimun_swaps(a)))
print('Should be 7 and returned: ' + str(minimun_swaps(b)))
