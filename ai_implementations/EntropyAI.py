import itertools
import math

from WordleAI import WordleAI, LetterInformation
from WordleJudge import WordleJudge

class EntropyAI(WordleAI):
    def __init__(self, words):
        super().__init__(words)
        self.judge = WordleJudge(words)
        self.cache = {}

    def guess(self, guess_history):
        candidates = self.words
        for (guess, outcome) in guess_history:
            for i, x in enumerate(outcome):
                if x == LetterInformation.CORRECT:
                    candidates = [x for x in candidates if x[i] == guess[i]]
                elif x == LetterInformation.PRESENT:
                    candidates = [x for x in candidates if x[i] != guess[i] and guess[i] in x]
                else:
                    candidates = [x for x in candidates if guess[i] not in x]
        return self.cached_get_candidate(candidates, self.words, guess_history)

    def get_author(self):
        return "Akshaylive"

    """
    This function provides three probability values:
    p[ch][i] -> probability of finding character at i out of all words
    q[ch][i] -> probability of finding character at a location other than i out of all words
    r[ch] -> probability of a character not being in any location out of all words
    """
    def get_probability_distributions(self, words):
        p = {}
        q = {}
        r = {}

        for k in range(26):
            k = chr(k + 97)
            p[k] = [0.0] * 5
            q[k] = [0.0] * 5
            r[k] = 0

        for word in words:
            for i, ch in enumerate(word):
                p[ch][i] += 1

        for word in words:
            for i, ch in enumerate(word):
                for j in range(5):
                    if word[j] != ch:
                        q[ch][j] += 1

        for word in words:
            for ch in set(word):
                r[ch] += 1

        for k in range(26):
            k = chr(k + 97)
            p[k] = [x / len(words) for x in p[k]]
            q[k] = [x / len(words) for x in q[k]]
            r[k] = 1 - r[k] / len(words)

        return p, q, r

    def safe_entropy(self, p):
        return p * math.log(p) if p != 0 else 0

    def get_score(self, word, p, q, r):
        entropy = 0
        frequency = {}
        for ch in word:
            frequency[ch] = frequency.get(ch, 0) + 1
        for i, ch in enumerate(word):
            entropy -= self.safe_entropy(p[ch][i])
            entropy -= self.safe_entropy(q[ch][i]) / frequency[ch] # special assumption when a character is repeated more than once
            entropy -= self.safe_entropy(r[ch])
        return entropy

    def cached_get_candidate(self, words, all_words, guess_history):
        key = tuple(itertools.chain(*[[x[0]]+x[1] for x in guess_history]))
        if key in self.cache:
            return self.cache[key]
        value = self.get_candidate(words, all_words)
        if len(guess_history) < 2:
            self.cache[key] = value
        return value

    def get_candidate(self, words, all_words):
        m = 0
        best = words[0]
        p, q, r = self.get_probability_distributions(words)

        # Once the number of words become small enough, restrict search to that.
        if len(words) <= 2:
            all_words = words

        for word in all_words:
            s = self.get_score(word, p, q, r) + self.judge.is_wordle_probability(word)
            if s > m:
                m = s
                best = word
        return best
