# given a list of complete words and a semi-complete word, return a list of every
# completion of the semi-complete word

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_word(self, word):
        if not word:
            return
        char = word[0]

        if char in self.children:
            self.children[char].add_word(word[1:])
        else:
            child = Node(char)
            self.children[child.value] = child
            child.add_word(word[1:])

    def __repr__(self):
        if self.value:
            return self.value
        else:
            return 'Root of the Trie'


def build_trie(words):
    trie = Node('')
    # for each word in words...
    # scan the characters in the word
    # populating the trie as we scan
    for word in words:
        trie.add_word(word)
    return trie


def complete_words(semi, trie):
    complete = []
    word = ''
    if not semi:
        return complete
    # traverse the trie to semi
    # populate complete with each descendant
    complete_words_helper(semi, trie, complete, word)
    return complete


def complete_words_helper(semi, node, complete, word):
    # check the edge case that semi does not exist in the autocomplete set
    if semi and not node.children:
        complete = []
    # check the base case
    # populating complete with autocorrect word
    elif not node.children:
        complete.append(word)
    # traverse the trie until we have found the node that represents last of the semi-complete
    elif semi:
        word += semi[0]
        char = semi[0]
        if char in node.children:
            complete_words_helper(semi[1:], node.children[char], complete, word)
    # traverse the descendants of the semi-complete
    else:
        for k, v in node.children.items():
            complete_words_helper(semi, node.children[k], complete, word + k)


def autocomplete(words, semi):
    # build a trie
    trie = build_trie(words)
    # evaluate the semi-complete word against the trie
    complete = complete_words(semi, trie)

    return complete


# test data
words = ['dog', 'door', 'dark', 'cat', 'elephant']
semi = 'd'

# driver call
print(autocomplete(words, semi))