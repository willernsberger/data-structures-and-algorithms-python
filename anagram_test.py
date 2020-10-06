# given a longer string and a shorter string, determine if an anagram of the
# shorter string could be found as a substring of the longer string


# O(n) time
# O(1) space as the size of the anagram dictionary is bounded
# by the size of the alphabet
def anagram_test(shorter, longer):
    # edge cases
    if len(shorter) == 0 or len(shorter) > len(longer):
        return False
    # create a dictionary representing an anagram
    anagram = {}
    for char in shorter:
        if char in anagram:
            anagram[char] += 1
        else:
            anagram[char] = 1
    # as we evaluate the longer string, increment or decrement the count
    # of letters in the anagram
    for index in range(0, len(longer) - len(shorter) + 1):
        # we start out by decrementing the anagram until we are at an index
        # that matches the lenght of the anagram
        if index < len(shorter):
            char = longer[index]
            if char in anagram:
                anagram[char] -= 1
                if anagram[char] == 0:
                    anagram.pop(char)
            else:
                anagram[char] = -1
        # once we are at an index that matches the length of the anagram
        # we continue to modify the anagram
        else:
            # remove index - len(shorter)
            char = longer[index - len(shorter)]
            if char in anagram:
                anagram[char] += 1
                if anagram[char] == 0:
                    anagram.pop(char)
            else:
                anagram[char] = 1
            # add index
            char = longer[index]
            if char in anagram:
                anagram[char] -= 1
                if anagram[char] == 0:
                    anagram.pop(char)
            else:
                anagram[char] = -1
        # evaluate after each iteration
        if len(anagram) == 0:  # we win!
            return True

    return False


# testing
long = 'adcbacdacb'
short = 'abc'

# driver
print(anagram_test(short, long))  # True
