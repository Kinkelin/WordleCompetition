from collections import defaultdict, Counter
import inspect
import os
import random
import importlib
import time

import pytablewriter
import numpy as np
from pytablewriter.style import Style

from WordList import *
from WordleAI import *
from ai_implementations import LetterPopularityAI


class Competition:

    def __init__(self, competitor_directory, wordlist_filename="data/official/combined_wordlist.txt", hard_mode=False):
        self.competitor_directory = competitor_directory
        self.wordlist = WordList(wordlist_filename)
        self.words = self.wordlist.get_list_copy()
        self.competitors = self.load_competitors()
        self.hard_mode = hard_mode

    def load_competitors(self):
        competitors = []
        for file in os.listdir(self.competitor_directory):
            if file.endswith(".py"):
                module = importlib.import_module(self.competitor_directory + "." + file[:-3])
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, WordleAI) and not inspect.isabstract(obj):
                        competitors.append(obj(self.wordlist.get_list_copy()))

        return competitors

    def guess_is_legal(self, guess, guess_history):
        return len(guess) == 5 and guess.lower() == guess and guess in self.words and (
                not self.hard_mode or is_hard_mode(guess, guess_history))

    def play(self, competitor, word):
        guesses = []
        success = False
        guess_history = []

        for i in range(6):  # Up to 6 guesses
            guess = competitor.guess(guess_history)
            if not self.guess_is_legal(guess, guess_history):
                print("Competitor ", competitor.__class__.__name__, " is a dirty cheater!")
                print("hard_mode: ", self.hard_mode, "guess: ", guess, "guess_history", guess_history)
                print("Competition aborted.")
                quit()

            guess_result_dict = defaultdict(lambda: None)
            counted = dict(Counter(word))

            # first time around we check for well-placed letters
            # as it's "free", we also check for letters that are not present
            for c in range(5):
                if guess[c] not in word:
                    guess_result_dict[c] = LetterInformation.NOT_PRESENT
                elif word[c] == guess[c]:
                    guess_result_dict[c] = LetterInformation.CORRECT
                    # signal this letter has already be used once
                    counted[guess[c]] -= 1
            # second time around, we check for letter that ar present but misplaced
            # since we already checked well-placed letter, a letter that is present twice in the
            # guess will be accounted correctly
            for c in range(5):
                if guess_result_dict[c] is not None:
                    continue
                if counted[guess[c]] > 0:
                    guess_result_dict[c] = LetterInformation.PRESENT
                    # let's not forget to update how many of that letter rmain in the original word
                    counted[guess[c]] -= 1
                else:
                    guess_result_dict[c] = LetterInformation.NOT_PRESENT

            # transform guess_result back to a list
            guess_result = [guess_result_dict[c] for c in range(5)]

            guess_history.append((guess, guess_result))
            guesses.append(guess)

            if guess == word:
                success = True
                break
        return success, guesses

    def fight(self, rounds, print_details=False, solution_wordlist_filename='data/official/combined_wordlist.txt',
              shuffle=False):
        print("Start tournament")
        result = {}
        success_total = {}
        guesses = {}
        points = {}
        round_words = []

        for competitor in self.competitors:
            result[competitor] = 0
            success_total[competitor] = 0
            guesses[competitor] = []
            points[competitor] = []
        fight_words = WordList(solution_wordlist_filename).get_list_copy()
        start = time.time()
        competitor_times = np.zeros(len(self.competitors))
        for r in range(rounds):
            word = random.choice(fight_words) if shuffle else fight_words[r]
            current_time = time.time() - start
            round_words.append(word)
            c = 0
            for competitor in self.competitors:
                print("\rRound", r + 1, "/", rounds, "word =", word, "competitior", c + 1, "/", len(self.competitors),
                      "time", current_time, "/", current_time * rounds / (r + 1), end='')
                competitor_start = time.time()
                success, round_guesses = self.play(competitor, word)
                round_points = len(round_guesses) if success else 10
                result[competitor] += round_points
                guesses[competitor].append(round_guesses)
                points[competitor].append(round_points)
                if success:
                    success_total[competitor] += 1
                competitor_times[c] += time.time() - competitor_start
                c += 1

        print("\n")
        for i in range(len(competitor_times)):
            print(self.competitors[i].__class__.__name__, "calculation took", "{:.3f}".format(competitor_times[i]), "seconds")

        print("")
        if print_details:
            print("Words: ", round_words)
            print("Guesses: ", guesses)
            print("Points per round: ", points)
            print("")

        print("Competition finished with ", rounds, " rounds, ", len(self.competitors), " competitors and hard_mode = ", self.hard_mode,"\n")
        result = dict(sorted(result.items(), key=lambda item: item[1]))

        writer = pytablewriter.MarkdownTableWriter()
        writer.table_name = "Leaderboard"
        writer.headers = ["Nr", "AI", "Author", "Points per round", "Success rate"]
        for i in range(len(writer.headers)):
            writer.set_style(column=i, style=Style(align="left"))
        writer.value_matrix = []

        placement = 1
        for competitor in result:
            writer.value_matrix.append(
                [placement, competitor.__class__.__name__, competitor.get_author(), result[competitor] / rounds,
                 str(100 * success_total[competitor] / rounds) + "%"])
            placement += 1
        writer.write_table()


def is_hard_mode(word, guess_history):
    """
    Returns True if the word is a legal guess in hard mode.
    """
    return len(LetterPopularityAI.remaining_options([word], guess_history)) == 1


def main():
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(suppress=True)

    competition = Competition("ai_implementations", wordlist_filename="data/official/combined_wordlist.txt", hard_mode=False)
    competition.fight(rounds=1000, solution_wordlist_filename="data/official/shuffled_real_wordles.txt", print_details=False)

if __name__ == "__main__":
    main()
