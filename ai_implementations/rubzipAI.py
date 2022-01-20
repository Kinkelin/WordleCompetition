import string

import math as m
from WordleAI import WordleAI, LetterInformation

class RubzipAI(WordleAI):

    def guess(self, revealed, letters, guess_history, attempts, hard_mode):
        known_letters = calculate_known_letters(revealed) # What letters we know where excatly there are
        options = remaining_options(self.words, guess_history)  # take known information into account
        if(len(options)==1):
            best_option = options[0]
        else:
            letter_popularity = calculate_letter_entropy(options, known_letters)  # calculate letter popularity in remaining options

            use_all_words = (attempts % 3) != 0 #We use the possible words only on the third and sixth attempts
            if(use_all_words):
            	options = self.words

            best_option = options[0]
            highest_popularity = 0
            for option in options:  # looks through all the options
                popularity = calculate_word_popularity(option, letter_popularity)
                if popularity > highest_popularity:
                    best_option = option  # store the best option found
                    highest_popularity = popularity
        return best_option


def calculate_letter_entropy(words, known_letters):#EDITED BY ME
    letter_popularity = dict.fromkeys(list(string.ascii_lowercase), 0)
    total = 1
    for word in words:
        for letter in word:#¿SET OR NOT?
            if(letter not in known_letters):#If we know the position of a letter this doesnt gives us information
                letter_popularity[letter] += 1  # each occurance of the letter is counted
                total += 1
    for letter in letter_popularity:#Based on the frec of every letter we are going to calculate the shannon entropy
        prob = letter_popularity[letter]/total
        if(prob!=0):
            letter_popularity[letter] = -prob*m.log2(prob)

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


def calculate_known_letters(revealed):#EDITED BY ME
    known_letters = set(revealed.replace('_', ''))

    return known_letters


