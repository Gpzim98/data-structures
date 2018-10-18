# Dynamic programming (Hash table for memoization + recursion )
# All constant time operation O( 1 ) when summed up is O(1)
# The recursive part have the execution time = O(2n + 1)
# O(2n + 1) * O(1) = O(2n + 1)
# Drop constant = O(n)
memo = {}


def fib(n, memo):
    if n in [1, 2]:  # Constant time operation O(1)
        return 1   # Constant time operation O(1)
    elif n in memo.keys():  # Constant time operation O(1)
        return memo[n]  # Constant time operation O(1)
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)  # O(2n + 1)
        memo[n] = result  # O(1)
    return result  # O(1)


print(fib(500, memo))
