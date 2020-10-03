import heapq

# given an unsorted array of numbers, find the kth largest element
# there are multiple posisble solutions, with different implementations
# and runtimes


# O(kn^2) brute force solution, iterating the array to find the largest element
# and removing it until we have removed kth largest
def find_kth_largest(arr, k):
    largest = 0
    largest_index = 0

    # find it k times...
    for i in range(0, k):
        # find the largest and remove it
        largest = arr[0]
        for j in range(0, len(arr)):
            if arr[j] >= largest:
                largest = arr[j]
                largest_index = j
        print(largest)
        arr.pop(largest_index)
    # return the most recent max element
    return largest


# O(nlog(n)) sort the array, return the element k from last in the array
def find_kth_largest_2(arr, k):
    arr.sort()
    return arr[-k]


# O(nlog(n)) build a heap, remove k elements from the heap, returning the last element removed
def find_kth_largest_3(arr, k):
    largest = 0
    # heapify the array
    arr = list(map(lambda x: -x, arr))
    heapq.heapify(arr)
    for i in range(0, k):
        largest = -heapq.heappop(arr)
    return largest


def partition(arr, start, end):
    sliced = arr[start:end + 1]
    print(str(sliced))
    pivot = arr[end]
    index = start
    # scan through every value in the array (except the pivot)
    # if the value is less than the pivot, swap it with the value
    # at the index position and increment the index position
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[index], arr[i] = arr[i], arr[index]
            index += 1
    # swap the pivot into position in the array
    arr[end], arr[index] = arr[index], arr[end]
    sliced = arr[start:end + 1]
    print(str(sliced))
    return index


# O(n) expected performance, O(n^2) worst case performance
def quick_select(arr, k):
    kth_index = len(arr) - k
    left = 0
    right = len(arr) - 1
    index = partition(arr, left, right)

    while True:
        # if we call partition and find k, we win!
        if index == kth_index:
            return arr[index]
        # if we call partition and index < k, we need to call partition again,
        # this time the range of the partition is upstream of the current index
        if index < kth_index:
            left = index + 1
            index = partition(arr, left, right)
            continue
        # if we call partition and index > k, we need to call partition again
        # this time the range of the partition is downstream of the current index
        if index > kth_index:
            right = index - 1
            index = partition(arr, left, right)
            continue


# testing data
k = 3  # 13
arr = [1, 8, 2, 6, 11, 4, 3, 15, 7, 0, 10, 12, 5, 14, 13, 9]

# driver function
print(quick_select(arr, k))