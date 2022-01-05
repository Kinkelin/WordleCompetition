from abc import ABC, abstractmethod
from enum import Enum, auto


class LetterInformation(Enum):
    UNKOWN = auto()  # light grey in the game
    PRESENT = auto()  # yellow in the game
    NOT_PRESENT = auto()  # dark grey in the game
    POSITION_KNOWN = auto()  # green in the game


def is_hard_mode(word, revealed, letters):
    """
    Returns True if the word is a legal guess in hard mode.

    Parameters
    ----------
    word : str
        A 5 letter word in lowercase

    revealed : str
            Contains the already revealed letters of the wordle. Unknown letters are replaced by '_' characters.
            Example: s____t (worlde is 'secret')

    letters : a dictionary holding letter:LetterInformation pairs
        Holds a LetterInformation enum value for each letter of the alphabet
    """
    for i in range(len(revealed)):
        if revealed[i] != '_' and revealed[i] != word[i]:
            return False

    for letter in letters:
        if letters[letter] == LetterInformation.PRESENT and letter not in word:
            return False

    return True


class WordleAI(ABC):

    def __init__(self, words):
        self.words = words  # list of all legal 5 letter words

    @abstractmethod
    def guess(self, revealed, letters, attempts, hard_mode):
        """
        Returns a 6 letter word trying to guess the wordle.

        Parameters
        ----------
        revealed : str
            Contains the already revealed letters of the wordle. Unknown letters are replaced by '_' characters.
            Example: s____t (worlde is 'secret')

        letters : a dictionary holding letter:LetterInformation pairs
            Holds a LetterInformation enum value for each letter of the alphabet

        attempts : int
            The number of previous attempts. Can contain a number from 0 to 4

        hard_mode : bool
            If True, the guess has to contain all present letters and known letters also in the right position
        """
        pass
