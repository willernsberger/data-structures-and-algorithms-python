# given, k, print the kth fibonacci number

def recursive_fib(k):
    # base cases
    if k == 0:
        return 1
    if k == 1:
        return 1
    return recursive_fib(k-1) + recursive_fib(k-2)


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
print(iterative_fib(k))