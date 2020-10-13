# Given an ordered array, find the fixed point in sublinear time.
# A fixed point is an item in the array where the value
# is equal to the index.


def fixed_point(arr):
    start = 0
    end = len(arr) - 1
    index = (end - start)//2
    while(True):
        if arr[index] == index:
            return index
        elif start == end:
            return False
        elif arr[index] > index:
            end = index - 1
        elif arr[index] < index:
            start = index + 1
        index = start + (end - start)//2


# driver
print(fixed_point([-1, 0, 1, 2, 3, 4, 5, 6, 8]))  # 8
print(fixed_point([0, 2, 3, 4, 5, 6, 8]))  # 0
print(fixed_point([-1, 0, 1, 3, 4, 5, 6, 8]))  # 3
print(fixed_point([-2, -1, 0, 1, 2, 3, 4, 6, 7, 8]))  # False
