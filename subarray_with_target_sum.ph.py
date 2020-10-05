# given an array and a target sum,
# find the first subarray within the given array
# which adds up to the target sum


# O(n^3) time for the two nested for-loops and the summation
def target_subarray_brute_force(arr, value):
    subarray = []

    for start in range(0, len(arr)):
        for end in range(start, len(arr)):
            subarray_sum = sum(arr[start:end + 1])
            if subarray_sum == value:
                subarray = [start, end]
                return subarray

    return subarray



def target_subarray_pointer_manipulation(arr, value):
    subarray = []

    start, end = 0, 0
    while start < len(arr) and end < len(arr):
        subarray_sum = sum(arr[start:end + 1])
        if subarray_sum == value:
            subarray = [start, end]
            return subarray
        elif start == end and subarray_sum > value:
            start += 1
            end += 1
        elif subarray_sum < value:
            end += 1
        elif subarray_sum > value:
            start += 1

    return subarray



# testing
arr = [1, 3, 2, 5, 7, 2, 4, 5, 9, 1, 4, 100]
value = 100

# driver
print(target_subarray_brute_force(arr, value))
