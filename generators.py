# Sample usage of generators.

# You can create a generator object with the yield statement.
# The generator object take an iterable and an expression.
# The generator iterates over the iterable,
# yielding a single result upon each execution.
# This is useful beacuse it allows you to iterate over the
# iterable, storing only one result of the expression in memory
# at a time (instead of the entire results set).
# With millions of items in the iterable that could otherwise get quite large.

# # Sample generator definition and usage
# def square(my_nums):
#     for i in my_nums:
#         yield (i*i)
#
# square_gen = square([1, 2, 3, 4, 5])
# for i in square_gen:
#     print(i)

# # Generators can be defined inside a comprehension
# my_nums = [1, 2, 3, 4, 5]
# square_gen = (i*i for i in my_nums)
# for i in square_gen:
#     print( i)

# You can use the generator to pooulate a list by
# just calling the list function, but this will
# create a list which now stores the entire generator
# result set in memory.
my_nums = [1, 2, 3, 4, 5]
square_gen = list((i*i for i in my_nums))
for i in square_gen:
    print( i)
