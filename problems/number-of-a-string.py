def repeatedString(s, n):
    # index = 0
    # count_a = 0
    #
    # if s == 'a':
    #     return n
    #
    # for i in range(0, n):
    #
    #     if s[index] == 'a':
    #         count_a += 1
    #     index = (index + 1) if (index + 1) < len(s) else 0
    count = s.count('a')
    mod = n % len(s)
    tot = (n // len(s)) * count
    count_a = 0

    for i in range(0, mod):
        if s[i] == 'a':
            count_a += 1

    return tot + count_a

assert repeatedString('jdiacikk', 899491) == 112436
assert repeatedString('aba', 10) == 7
assert repeatedString('beeaabc', 711560125001) == 203302892858
assert repeatedString('gfcaaaecbg', 547602) == 164280