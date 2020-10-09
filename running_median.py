# Given a list of numbers, find the running median at each index.
import heapq


def running_median(numbers):
    # "lesser" heap is a max heap
    # "greater" heap is a min heap
    lesser_heap = []
    greater_heap = []
    medians = []
    for index in range(0, len(numbers)):
        # bootstrap
        if index == 0:
            lesser_heap.append(-numbers[index])
            medians.append(get_median(lesser_heap, greater_heap))
            continue
        # evaluate which heap to place the element in
        place_number(numbers[index], lesser_heap, greater_heap)
        # rebalance the heaps
        rebalance_heaps(lesser_heap, greater_heap)
        # add the running median to the medians list
        medians.append(get_median(lesser_heap, greater_heap))
    return medians


def place_number(number, lesser_heap, greater_heap):
    if number > -lesser_heap[0]:
        heapq.heappush(greater_heap, number)
    else:
        heapq.heappush(lesser_heap, -number)


def rebalance_heaps(lesser_heap, greater_heap):
    if len(lesser_heap) > len(greater_heap) + 1:
        item = -heapq.heappop(lesser_heap)
        heapq.heappush(greater_heap, item)
    elif len(lesser_heap) < len(greater_heap) - 1:
        item = heapq.heappop(greater_heap)
        heapq.heappush(lesser_heap, -item)


def get_median(lesser_heap, greater_heap):
    if len(lesser_heap) > len(greater_heap):
        return -lesser_heap[0]
    elif len(lesser_heap) < len(greater_heap):
        return greater_heap[0]
    else:
        median = (-lesser_heap[0] + greater_heap[0]) / 2.0
        return median


# Test data
test_numbers = [2, 1, 4, 7, 2, 0, 5]

# driver
print(running_median(test_numbers))
