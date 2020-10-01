# given an ordered list of stock prices, determine the maximum profit

def maximum_profit(prices):
    # initialize
    floor = prices[0]
    floor_index = 0
    index = 1
    profit = prices[floor_index + 1] - floor
    while index < len(prices):
        # find a smaller value than the current floor
        if prices[index - 1] < floor:
            floor = prices[index - 1]
            floor_index = index
        # evaluate each following price for a profit
        # update max_profit if we find a new max
        if (prices[index] - floor) > profit:
            profit = prices[index] - floor
        # increment the index position
        index += 1
    return profit

print(maximum_profit([9, 11, 8, 5, 7, 10]))