from WordList import WordList


class WordleJudge:
    """
    Helper class to take into account how common words are in the English language.
    """

    def __init__(self, words=WordList("data/official/combined_wordlist.txt").words,
                 common_words=WordList("data/other/common_words.txt").words):
        self.common_words = common_words
        self.probability = {}
        for word in words:
            self.probability[word] = self.__calculate_probability(word)

    def __calculate_probability(self, word):
        if word not in self.common_words:
            return 368 / (368 + 8890)
        relative_position = self.common_words.index(word) / len(self.common_words)
        return 0.85 * (1 - relative_position) + 0.35 * relative_position

    def is_wordle_probability(self, word):
        """
        :param word: a 5 letter word
        :return: the probability of the word being a wordle based on its popularity in the English language
        """
        return self.probability[word]
