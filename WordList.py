class WordList:

    def __init__(self, filename):
        with open(filename) as file:
            self.words = file.readlines()
            self.words = [word.rstrip() for word in self.words]
            self.words = list(filter(lambda w: len(w) == 5 and w.isalpha() and w.lower() == w and len(set(w)) == 5, self.words))

    def get_list(self):
        return self.words.copy()
