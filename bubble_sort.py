a = [10, 9, 8, 7, 6, 5, 4, 3]
a = [10, 9, 8, 7]

unsorted = True
index = 0

while unsorted:
    unsorted = False

    prev = a[index]
    next = a[index + 1]
    size = len(a)
    size1 = (index + 1)

    has_next = size1 < size

    if has_next and (prev > next):
        a[index], a[index + 1] = a[index + 1], a[index]
        unsorted = True
        index += 1

    elif index > 1:
        index = 0
        unsorted = True

print(a)
