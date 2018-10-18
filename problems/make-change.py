"""
Check out the resources on the page's right side to learn more about dynamic
programming. The video tutorial is by Gayle Laakmann McDowell, author of the
best-selling interview book Cracking the Coding Interview.

Given a number of dollars and an array of denominations of coins, determine
how many ways you can make change. For example, making change for  dollars
from coin denominations , there are  ways to make change:


4 3
1 2 3

Rest = 4
"""
#!/bin/python3

import os

# Complete the ways function below.
def ways(n, coins):
    combinations = [0] * (n + 1)
    combinations[0] = 1

    for coin in coins:
        for i in range(0, len(combinations)):
            if i >= coin:
                combinations[i] += combinations[i - coin]

    return combinations[n]

ways(12, [1, 2, 5])


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     coins = list(map(int, input().rstrip().split()))
#
#     res = ways(n, coins)
#
#     fptr.write(str(res) + '\n')
#
#     fptr.close()