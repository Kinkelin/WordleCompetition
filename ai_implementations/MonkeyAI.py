import random

from WordleAI import WordleAI


class MonkeyAI(WordleAI):

    def guess(self, revealed, letters, guess_history, attempts, hard_mode):
        return random.choice(self.words)