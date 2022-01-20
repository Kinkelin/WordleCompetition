import string

from WordleAI import WordleAI, LetterInformation


class LetterPopularityAI(WordleAI):
    """
    This AI looks at letter popularity in a word list and picks the word with the highest letter popularity.
    """

    def guess(self, guess_history):
        options = remaining_options(self.words, guess_history)  # take known information into account
        letter_popularity = calculate_letter_popularity(options)  # calculate letter popularity in remaining options
        best_option = options[0]
        highest_popularity = 0
        for option in options:  # looks through all the options
            popularity = calculate_word_popularity(option, letter_popularity)
            if popularity > highest_popularity:
                best_option = option  # store the best option found
                highest_popularity = popularity
        return best_option

    def get_author(self):
        return "example"


def calculate_letter_popularity(words):
    letter_popularity = dict.fromkeys(list(string.ascii_lowercase), 0)
    for word in words:
        for letter in word:
            letter_popularity[letter] += 1  # each occurance of the letter is counted
    return letter_popularity


def calculate_word_popularity(word, letter_popularity):
    word_popularity = 0
    for letter in set(word):  # don't count double letters
        word_popularity += letter_popularity[letter]  # word popularity = sum of its letter popularities
    return word_popularity


def remaining_options(words, guess_history):
    """
    Filters a word list with all the known information.
    Returns the list of remaining options.
    """
    present = set()
    not_present = set()
    correct = set()
    present_letters = set()
    for entry in guess_history:
        for i in range(5):
            if entry[1][i] == LetterInformation.CORRECT:
                correct.add((entry[0][i], i))
                present_letters.add(entry[0][i])
            elif entry[1][i] == LetterInformation.PRESENT:
                present.add((entry[0][i], i))
                present_letters.add(entry[0][i])
            else:
                not_present.add(entry[0][i])

    for c in present_letters:
        words = [w for w in words if c in w]
    for c in not_present:
        words = [w for w in words if c not in w]
    for c in correct:
        words = [w for w in words if w[c[1]] == c[0]]
    for c in present:
        words = [w for w in words if w[c[1]] != c[0]]

    return words
