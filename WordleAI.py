from abc import ABC, abstractmethod
from enum import Enum, auto


class LetterInformation(Enum):
    UNKOWN = auto()  # light grey in the game
    PRESENT = auto()  # yellow in the game
    NOT_PRESENT = auto()  # dark grey in the game
    CORRECT = auto()  # green in the game


class WordleAI(ABC):

    def __init__(self, words):
        self.words = words  # list of all legal 5 letter words

    @abstractmethod
    def guess(self, guess_history):
        """
        Returns a 5 letter word trying to guess the wordle.

        Parameters
        ----------
        guess_history : list of tuples (guess, result)
            A list of tuples (word, result) with result consisting of LetterInformation for each letter on their
            position specifically, for example one previous guess with the guess 'steer' for the word 'tiger':
            [('steer',[LetterInformation.NOT_PRESENT, LetterInformation.PRESENT,
            LetterInformation.PRESENT, LetterInformation.CORRECT, LetterInformation.CORRECT])]
        """
        pass

    @abstractmethod
    def get_author(self):
        """
        Returns the name of the author
        """
        pass
