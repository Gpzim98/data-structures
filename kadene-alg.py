a = [-2, 3, 2, -1, 7, 7, 0, 9]

def kadene(a):
    max_current, max_global = a[0], a[0]

    _range = range(1, len(a))
    for i in _range:
        max_current = a[i] if a[i] >= max_current + a[i] else max_current + a[i]

        if max_current > max_global:
            max_global = max_current

    return max_global

print(kadene(a))
