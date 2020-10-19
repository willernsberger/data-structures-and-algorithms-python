# a few examples of using comprehensions

# list comprehensions
# new_list = [expression for member in iterable]
old_list = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in old_list]
print(new_list)

# new_list = [expression for member in iterable if conditional]
old_list = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in old_list if n > 3]
print(new_list)

# new_list = [function for member in iterable]
old_list = [1, 2, 3, 4, 5]
def function(n):
    return n*n
new_list = [function(n) for n in old_list]
print(new_list)

# new_list = [expression function for member in iterable if conditional]
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = [1, 2, 3, 5, 7, 11]
def function(n):
    return n*n
new_list = [function(n) for n in old_list if n in primes]
print(new_list)

# new_list = [expression function for member in iterable if conditional function]
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def is_prime(n):
    primes = [1, 2, 3, 5, 7, 11]
    if n in primes:
        return True
    return False
def function(n):
    return n*n
new_list = [function(n) for n in old_list if is_prime(n)]
print(new_list)

# new_list = [expression function conditional statement for member in iterable if conditional function]
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def is_prime(n):
    primes = [1, 2, 3, 5, 7, 11]
    if n in primes:
        return True
    return False
def function(n):
    return n*n
new_list = [function(n) if n > 3 else n + 1 for n in old_list if is_prime(n)]
print(new_list)

# new_list = [conditional function for member in iterable if conditional function]
old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def is_prime(n):
    primes = [1, 2, 3, 5, 7, 11]
    if n in primes:
        return True
    return False
def conditional_function(n):
    return n*n if n > 3 else n + 1
new_list = [conditional_function(n) for n in old_list if is_prime(n)]
print(new_list)

# set comprehension
# set comprehension is almost the same as list comprehension except
# that the output is a set (which enforces uniqueness of items)
new_set = {i%3 for i in range(10)}
print(new_set)

# dictionary comprehension
# dictionary comprehension is almost the same as list comprehension except
# that the output is a dictionary and the comprehension statement
# requires both the key and value
new_dictionary = {k: k*k for k in range(10)}
print(new_dictionary)
