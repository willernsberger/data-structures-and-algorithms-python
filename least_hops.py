# Given an array where each index in the array represents a postion
# and the value at that index represents the maximum number of
# spaces forward one could hop, determine the least number
# of hops it would take to get to the end of the array.


# Linear time with respect to the number of positions in the array.
# Constant space for a few variables.
def least_hops(positions):
    position = 0
    hops = 0
    while position < len(positions) - 1:
        # look ahead
        distance = look_ahead(position, positions)
        # hop
        position += distance
        hops += 1
    return hops


def look_ahead(start_position, positions):
    hop = positions[start_position]
    # return if we can finish in one hop
    if hop + start_position >= len(positions) - 1:
        return hop
    distance = 0
    max_double_hop_distance = 0
    for index in range(start_position + 1, start_position + hop + 1):
        # evaluate every hoppable position
        # return distance to whichever hoppable positon
        # gives the greatest double hop
        first_hop_distance = index - start_position
        double_hop_distance = first_hop_distance + positions[index]
        if double_hop_distance > max_double_hop_distance:
            max_double_hop_distance = double_hop_distance
            distance = first_hop_distance
    return distance


print(least_hops([3, 2, 5, 1, 1, 9, 4, 4]))  # 2 hops
