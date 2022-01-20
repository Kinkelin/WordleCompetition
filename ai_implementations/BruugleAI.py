# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 13:44:06 2022

@author: Bruugle
"""

from WordleAI import WordleAI, LetterInformation
from WordleJudge import WordleJudge

class BruugleAI(WordleAI):
    '''
    This AI uses a set of fixed guesses to narrow down the exact letters for the final guess.
    '''
    def __init__(self, words):
        super().__init__(words)
        self.magic_words = ["bemix", "grypt", "clunk", "waqfs", "vozhd"]
        self.corpus = words
        self.judge = WordleJudge()
    
    def guess(self, guess_history):
        guess_number = len(guess_history)
        if  guess_number < 5:
            next_guess = self.magic_words[guess_number]
        else:
            present_letters = [entry[0][i] for entry in guess_history for i in \
                range(5) if entry[1][i] == LetterInformation.PRESENT]
            forbidden_letters = [entry[0][i] for entry in guess_history for i in \
                range(5) if entry[1][i] == LetterInformation.NOT_PRESENT]
            correct_positions = [(entry[0][i], i) for entry in guess_history \
                for i in range(5) if entry[1][i] == LetterInformation.CORRECT]
            forbidden_positions = [(entry[0][i], i) for entry in guess_history \
                for i in range(5) if entry[1][i] == LetterInformation.PRESENT]
            word_pool = self.corpus
            word_pool = include(word_pool, present_letters)
            word_pool = exclude(word_pool, forbidden_letters)
            word_pool = include_positions(word_pool, correct_positions)
            word_pool = exclude_positions(word_pool, forbidden_positions)
            word_evaluations = [self.judge.is_wordle_probability(word) for word in word_pool]
            best_score = max(word_evaluations)
            next_guess = word_pool[word_evaluations.index(best_score)]
        return next_guess

    def get_author(self):
        return "Bruugle"


def include(word_list, values):
    filtered_word_list = word_list
    for value in values:
        filtered_word_list = [word for word in filtered_word_list if value in word]
    return filtered_word_list

def exclude(word_list, values):
    filtered_word_list = word_list
    for value in values:
        filtered_word_list = [word for word in filtered_word_list if not value in word]
    return filtered_word_list

def include_positions(word_list, values):
    filtered_word_list = word_list
    for value in values:
        filtered_word_list = [word for word in filtered_word_list if value[0] == word[value[1]]]
    return filtered_word_list

def exclude_positions(word_list, values):
    filtered_word_list = word_list
    for value in values:
        filtered_word_list = [word for word in filtered_word_list if not value[0] == word[value[1]]]
    return filtered_word_list