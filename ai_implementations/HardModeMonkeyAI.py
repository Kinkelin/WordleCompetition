import random

from WordleAI import WordleAI, is_hard_mode


class HardModeMonkeyAI(WordleAI):

    def guess(self, revealed, letters, guess_history, attempts, hard_mode):
        while True:
            word = random.choice(self.words)
            if is_hard_mode(word, revealed, letters):
                break

        return word
