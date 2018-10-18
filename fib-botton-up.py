# The complexity for this algorithm is O(n) Because it is a simple loop from
# 2 to N linearly The advantage of that is that don't have the problem with
# the recursion call stack being to big


def fib(n):
    botton_up = []
    if n in [1, 2]:
        return 1

    botton_up.append(1)
    botton_up.append(1)

    for i in range(2, n):
        botton_up.append(botton_up[i - 1] + botton_up[i - 2])

    return botton_up[n-1]

print(fib(500))
