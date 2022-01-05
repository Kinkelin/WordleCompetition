import random

from WordleAI import WordleAI


class MonkeyAI(WordleAI):

    def guess(self, revealed, letters, attempts, hard_mode):
        return random.choice(self.words)