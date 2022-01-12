import string

from WordleAI import WordleAI, LetterInformation


class LetterPopularityAI(WordleAI):
    """
    This AI looks at letter popularity in a word list and picks the word with the highest letter popularity.
    """

    def guess(self, revealed, letters, guess_history, attempts, hard_mode):
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
    return [word for word in words if fits_guess_history(word, guess_history)]


def fits_guess_history(word, guess_history):
    for entry in guess_history:
        for i in range(5):
            letter = entry[0][i]
            info = entry[1][i]
            if info == LetterInformation.CORRECT and word[i] != letter:
                return False
            if info == LetterInformation.PRESENT and (letter == word[i] or letter not in word):
                return False
            if info == LetterInformation.NOT_PRESENT and letter in word:
                return False
    return True