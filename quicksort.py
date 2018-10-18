arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]


a2 = []
a2.append(arr[0])
a2.append(arr[len(arr) // 2])
a2.append(arr[-1])
a2.sort()


pivot = a2[1]


def partition(a, low, hi):
    mid = (low + hi) // 2
    pivot = hi

    if a[low] < a[mid]:
        if a[mid] < a[hi]:
            pivot = mid
    elif a[low] < a[hi]:
        pivot = low

    return pivot



def quick_sort2(a, low, hi):
    if low < hi:
        p = partition(a, low, hi)
        quick_sort2(a, low, p - 1)
        quick_sort2(a, p + 1, hi)

def quick_sort(a):
    quick_sort2(a, 0, len(a) - 1)

quick_sort(arr)
print(arr)