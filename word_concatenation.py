# given a list of words, for each word in the list,
# determine if that word could be formed from a concatenation
# of other words in the words list.

# For a word of length m, the evaluation of the word is m^2 time
# with n words in the list, the overall time complexity is O(nm^2).
# Linear space complexity to build the words set, and linear
# space complexity for the evaluation call stack for
# an overall linear space complexity of O(n+m).
class Solution(object):
    def __init__(self, words):
        self.words = words
        self.words_set = set(words)
        self.concatenations = []

    def evaluate_word(self, word):
        # split the word into prefix and suffix
        # for each combination of start and end
        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in self.words_set and suffix in self.words_set:
                return True
            if prefix in self.words_set and self.evaluate_word(suffix):
                return True

    def find_concatentations(self):
        # for each word in the list, evaluate the word
        for word in self.words:
            if self.evaluate_word(word):
                self.concatenations.append(word)
        return self.concatenations


words_input = ['coffee', 'walk', 'pizza', 'snack', 'nap', 'z', 'pi', 'a']
s = Solution(words_input)
print(s.find_concatentations())
