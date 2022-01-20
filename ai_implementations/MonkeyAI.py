import random

from WordleAI import WordleAI


class MonkeyAI(WordleAI):

    def guess(self, guess_history):
        return random.choice(self.words)

    def get_author(self):
        return "example"