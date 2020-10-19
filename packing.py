# A few handy exmpales of packing and unpacking iterables.

# from itertools import zip_longest

# The zip function accepts iterables and returns a zip object which is an iterator of tuples.
# If the passed iterables have different lengths, the iterables with the least items decides
# the length of the new zip object iterator.
# names = ['Peter Parker', 'Clark Kent', 'Wade Wildson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# for name, hero in zip(names, heroes):
#     print(name + ' is  ' + hero)
#
# # Same as the previous example, this time using 3-tuples in the zip object
# names = ['Peter Parker', 'Clark Kent', 'Wade Wildson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']
# for name, hero, universe in zip(names, heroes, universes):
#     print(name + ' is  ' + hero + ' from ' + universe)

# If you want the longest iterables to define the length, use the ziplongest function
# from the itertools library.  Requires handling None types.
# names = ['Peter Parker', 'Clark Kent', 'Wade Wildson', 'Bruce Wayne', 'Spawn']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC', 'Image']
# for name, hero, universe in zip_longest(names, heroes, universes):
#     if name and hero and universe:
#         print(name + ' is  ' + hero + ' from ' + universe)

# # Alternately, we can store the tuple as a single value.
# names = ['Peter Parker', 'Clark Kent', 'Wade Wildson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']
# for value in zip(names, heroes, universes):
#     print(value)

# # Unpacking the zip object tuple.
# names = ['Peter Parker', 'Clark Kent', 'Wade Wildson', 'Bruce Wayne']
# heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
# universes = ['Marvel', 'DC', 'Marvel', 'DC']
# for value in zip(names, heroes, universes):
#     name, hero, universe = value
#     print(name + ' is  ' + hero + ' from ' + universe)

# # Some examples of packing and unpacking
# a, b = 1, 2
# print(a)
# print(b)
# c, d = (3, 4)
# print(c)
# print(d)
# e, f = [5, 6]
# print(e)
# print(f)
# tuple_a = (7, 8)
# g, h = tuple_a
# print(g)
# print(h)
# list_a = [9, 10]
# i, j = list_a
# print(i)
# print(j)
#
# # If you want to unpack into a variable which doesn't end up being used,
# # you can use an underscore which, by convention, lets Python and developers
# # know that the underscore variable is merely a placeholder.
# tuple_a = (11, 11.5)
# a, _ = tuple_a
# print(a)
#
# # Unpacking expects the same number of variables as unpacked elements.
# # Too many or too few variables will throw an error.
# tuple_d = (22, 23, 24, 25, 26)
# a, b, c = tuple_c  # throws an error, too few variables
# a, b, c, d, e, f, g = tuple_c  # throws an error, too few elements
#
# # You can unpack multiple elements into a single variable, using the asterisk syntax.
# # The multiple elements are unpacked into a list.
# tuple_b = (12, 13, 14, 15, 16)
# a, *b = tuple_b
# print(a)
# print(b)
#
# # You can unpack multiple elements into a single variable, followed by more single elements
# tuple_c = (17, 18, 19, 20, 21)
# a, *b, c = tuple_c
# print(a)
# print(b)
# print(c)
