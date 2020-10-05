# given, k, print the kth fibonacci number

# O(2^k) time
# O(k) space for the height of the recursion stack
def recursive_fib(k):
    # base cases
    if k == 0:
        return 1
    if k == 1:
        return 1
    return recursive_fib(k-1) + recursive_fib(k-2)


# O(k) time
# O(k) space for the map
def mapping_fib(k):
    m = {0: 1, 1: 1}
    for n in range(2, k+1):
        m[n] = m[n - 1] + m[n - 2]
    return m[k]


# O(k) time
# O(1) space for a few variables
def iterative_fib(k):
    # base cases
    if k == 0:
        return 1
    if k == 1:
        return 1

    previous_previous = iterative_fib(0)
    previous = iterative_fib(1)
    current = 2
    n = 2

    while n <= k:
        current = previous + previous_previous
        previous_previous = previous
        previous = current
        n += 1
    return current


# testing
k = 50

# driver
print(mapping_fib(k))