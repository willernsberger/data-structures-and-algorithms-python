from collections import deque

# given a grid with one color assigned to each square in the grid
# determine the maximum number of connected squares with the same color
# the grid does not wrap around
# squares connect up, down, left right
# linear time with respect to the number of squares as each is evaluated only once
# linear space as the elements on the queue and the number of elements in the
# deduplication map are bounded by the number of squares


def count_connected(grid, explored, row, column):
    count = 0
    color = grid[row][column]
    q = deque([])
    q.append((row, column))
    explored[row][column] = 'explored'
    while q:
        square = q.popleft()
        count += 1
        # add up to the queue
        if square[0] > 0 and explored[square[0] - 1][square[1]] != 'explored' and grid[square[0] - 1][square[1]] == color:
            q.append((square[0] - 1, square[1]))
            explored[square[0] - 1][square[1]] = 'explored'
        # add down to the queue
        if square[0] != len(grid) - 1 and explored[square[0] + 1][square[1]] != 'explored' and grid[square[0] + 1][square[1]] == color:
            q.append((square[0] + 1, square[1]))
            explored[square[0] + 1][square[1]] = 'explored'
        # add left to the queue
        if square[1] > 0 and explored[square[0]][square[1] - 1] != 'explored' and grid[square[0]][square[1] - 1] == color:
            q.append((square[0], square[1] - 1))
            explored[square[0]][square[1] - 1] = 'explored'
        # add right to the queue
        if square[1] != len(grid[square[0]]) - 1 and explored[square[0]][square[1] + 1] != 'explored' and grid[square[0]][square[1] + 1] == color:
            q.append((square[0], square[1] + 1))
            explored[square[0]][square[1] + 1] = 'explored'
    return count


def max_connected_colors(grid):
    # the largest number of connected colors
    maximum = 0
    # store the state of squares once checked
    # so they aren't checked repeatedly
    explored = list(grid)
    # iteration to check every position
    # breadth first search at each check that returns a count
    # update the max if the count is greater
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if explored[row][column] != 'explored':
                count = count_connected(grid, explored, row, column)
                maximum = max(maximum, count)
    return maximum


# test grid
grid = [
    ['white', 'black', 'white', 'white', 'white'],
    ['black', 'white', 'white', 'white', 'white'],
    ['black', 'white', 'black', 'white', 'white'],
    ['black', 'white', 'white', 'black', 'black'],
    ['white', 'black', 'black', 'black', 'black']
]

# driver function call  # 12
print(max_connected_colors(grid))