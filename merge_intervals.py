# given some intervals, merge the intervals into as few as possible.


# O(nlog(n)) time 
# O(n) space 
def merge_intervals(intervals):
    interval_start = -1
    interval_stop = -1
    counter = 0
    events = merge_intervals_helper(intervals)
    intervals = []
    for event in events:
        # if event is the first start, set interval start, increment count
        # if event is an interior start, increment counter
        if event[1] == "start":
            if counter == 0:
                interval_start = event[0]
            counter += 1
        # if event is a interior stop, decrement counter
        if event[1] == "stop":
            counter -= 1
            if counter == 0:
                interval_stop = event[0]
                interval = [interval_start, interval_stop]
                intervals.append(interval)
    return intervals

def merge_intervals_helper(intervals):
    # create a start and stop event from each interval in the intervals list
    events = []
    for interval in intervals:
        event = [interval[0], "start"]
        events.append(event)
        event = [interval[1], "stop"]
        events.append(event)
    events.sort(key=lambda x:x[0])
    for e in range(1, len(events)):
        if events[e][1] == "start" and events[e - 1][1] == "stop" and events[e][0] == events[e - 1][0]: 
            events[e][1], events[e - 1][1] = events[e - 1][1], events[e][1]
    return events

# 1-3  6-----10
#    4-6          20----25
intervals  = [[1, 3], [4, 6], [6, 10], [20, 25]]

print(merge_intervals(intervals))
# [[1, 3], [4, 10], [20, 25]]