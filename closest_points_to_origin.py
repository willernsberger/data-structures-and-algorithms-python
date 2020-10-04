import heapq
import math

# given an origin and  some points, find the k points closest to the origin


def calculate_distance(point):
    distance = point[0]*point[0] + point[1]*point[1]
    distance = math.sqrt(distance)
    return distance


# O(nlog(n)) time for the sort
def closest_points_to_origin(points, k):
    # evaluating each point in the list of points
    # sorted by the distance from the orgin
    points = sorted(points, key = lambda x: calculate_distance(x))
    return points[:k]


# O(n) time to build the heap, O(klog(n)) to find k least distances
# O(n) space for the heap data structure
def closest_points_to_origin_heap(points, k):
    data = []
    for p in points:
        data.append((calculate_distance(p), p))
    heapq.heapify(data)
    result = []
    for p in range(k):
        result.append(heapq.heappop(data)[1])
    return result

# testing data
k = 5
points = [[-1, -5], [-1, 5], [5, 5], [6, 5],
          [-3, 3], [3, 10], [-3, -3], [5, -4],
          [10, -6], [-3, -8], [15, -2], [-10, 5]]

# driver
print(str(closest_points_to_origin_heap(points, k)))
