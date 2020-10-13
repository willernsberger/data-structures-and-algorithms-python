# Given a list of publications, determine the H index.
# The H index is determined by counting the
# citations of each publication and finding
# the largest number which is the count of publications
# each of which have that number of citations (or more).


# Quadratic time complexity to populate the citations list
# followed by linear time complexity to evaluate the citations list.
# Linear space complexity for the citations list with respect to
# the number of publications.
def h_index_quadratic(publications):
    total = len(publications)
    citations = [0] * (total + 1)
    h = 0
    for publication in publications:
        publication = min(publication, total)
        while publication >= 0:
            citations[publication] += 1
            publication -= 1
    for index in range(0, len(citations)):
        if citations[index] >= h and index >= h:
            h = index
        print(h)
    return h


# Linear time complexity to populate the citations list
# followed by linear time complexity to evaluate the citations list
# for a total time complexity of linear with respec to the
# number of publications.
# Linear space complexity for the citations list with respect to
# the number of publications.
def h_index(publications):
    total = len(publications)
    citations = [0] * (total + 1)
    for publication in publications:
        publication = min(publication, total)
        citations[publication] += 1
    score = 0
    for index in range(-1, -len(citations), -1):
        score += citations[index]
        if score >= len(citations) + index:
            return score
    return score


print(h_index([0, 7, 3, 1, 3]))
