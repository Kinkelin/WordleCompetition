import inspect
import os
import string
import random
import importlib

from WordList import WordList
from WordleAI import LetterInformation, is_hard_mode, WordleAI


class Competition:

    def __init__(self, competitor_directory, hard_mode=False):
        self.competitor_directory = competitor_directory
        self.wordlist = WordList("word_list_long.txt")
        self.words = self.wordlist.get_list()
        self.competitors = self.load_competitors()
        self.hard_mode = hard_mode

    def create_letter_dictionary(self):
        dictionary = {}
        for letter in string.ascii_lowercase:
            dictionary[letter] = LetterInformation.UNKOWN
        return dictionary

    def load_competitors(self):
        competitors = []
        for file in os.listdir(self.competitor_directory):
            if file.endswith(".py"):
                module = importlib.import_module(self.competitor_directory + "." + file[:-3])
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, WordleAI) and not inspect.isabstract(obj):
                        competitors.append(obj(self.wordlist.get_list()))

        return competitors

    def replace_char(self, original_string, char_index, new_char):
        new_string = ""
        for i in range(len(original_string)):
            new_string +=  new_char if i == char_index else original_string[i]
        return new_string

    def guess_is_legal(self, guess, revealed, letters):
        return len(guess) == 5 and guess.lower() == guess and (
                    not self.hard_mode or is_hard_mode(guess, revealed, letters))

    def play(self, competitor, word):
        revealed = "_____"
        letters = self.create_letter_dictionary()
        guesses = []
        success = False

        for i in range(6):  # Up to 6 guesses
            guess = competitor.guess(revealed, letters, i, self.hard_mode)

            if not self.guess_is_legal(guess, revealed, letters):
                print("Competitor ", competitor.__class__.__name__, " is a dirty cheater!")
                print( "hard_mode: ", self.hard_mode, "guess: ", guess, "revealed: ", revealed, "letters: ", letters)
                print("Competition aborted.")
                quit()

            for c in range(5):
                if guess[c] not in word:
                    letters[guess[c]] = LetterInformation.NOT_PRESENT
                elif word[c] == guess[c]:
                    revealed = self.replace_char(revealed, c, guess[c])
                    letters[guess[c]] = LetterInformation.POSITION_KNOWN
                elif letters[guess[c]] != LetterInformation.POSITION_KNOWN:
                    letters[guess[c]] = LetterInformation.PRESENT

            guesses.append(guess)

            if guess == word:
                success = True
                break

        return success, guesses

    def fight(self, rounds, print_details=False):
        result = {}
        guesses = {}
        points = {}

        for competitor in self.competitors:
            round_words = []
            result[competitor] = 0
            guesses[competitor] = []
            points[competitor] = []

        for r in range(rounds):
            word = random.choice(self.words)
            round_words.append(word)
            for competitor in self.competitors:
                success, round_guesses = self.play(competitor, word)
                round_points = len(round_guesses) if success else 10
                result[competitor] += round_points
                guesses[competitor].append(round_guesses)
                points[competitor].append(round_points)

        if print_details:
            print("Words: ", round_words)
            print("Guesses: ", guesses)
            print("Points per round: ", points)

        print("Competition finished with ", rounds, " rounds, ", len(self.competitors), " competitors and hard_mode = ", self.hard_mode)
        result = dict(sorted(result.items(), key=lambda item: item[1]))
        placement = 1
        for competitor in result:
            print(competitor.__class__.__name__, " placed ", placement, " with a score of ", result[competitor])
            placement += 1


def main():
    competiton = Competition("ai_implementations", hard_mode=False)
    competiton.fight(1000, False)
    print("")
    competiton = Competition("ai_implementations_hard_mode", hard_mode=True)
    competiton.fight(1000, False)

if __name__ == "__main__":
    main()
