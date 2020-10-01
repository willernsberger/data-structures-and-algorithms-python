# given a list of "valid words" and a phone number
# return all the words that appear in the valid words list
# which could have been constructed from the phone number

# the phone map takes up constant space complexity
# because it is at most 26 entries
phone_map = {
    "a": 2, "b": 2, "c": 2,
    "d": 3, "e": 3, "f": 3,
    "g": 4, "h": 4, "i": 4,
    "j": 5, "k": 5, "l": 5,
    "m": 6, "n": 6, "o": 6,
    "p": 7, "q": 7, "r": 7, "s": 7,
    "t": 8, "u": 8, "v": 8,
    "w": 9, "x": 9, "y": 9, "z": 9
}

# validate words is linear time complexity because it is a single
# scan across the entries in the words list
def validate_words(words, phone_number):
    valid_words = []
    # iterating across the list of words...
    # adding the word to the valid words list if it checks out
    for word in words:
        word_number = []
        for letter in word:
            word_number.append(phone_map[letter])
        if word_number == phone_number:
            valid_words.append(word)
    return valid_words


# given inputs: list of words and a phone number
words = ['dog', 'fish', 'cat', 'fog']
phone_number = [3, 6, 4]

# driver function call
print(str(validate_words(words, phone_number)))