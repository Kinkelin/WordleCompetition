from WordList import WordList
from WordleAI import LetterInformation
from ai_implementations.LetterPopularityAI import LetterPopularityAI

ai = LetterPopularityAI(WordList("data/official/combined_wordlist.txt").get_list_copy())

attempts = 0
guess_history = []
while attempts < 6:
    guess = ai.guess(None, None, guess_history, attempts, False)

    print("AI guesses ", guess)
    print("Please type a response: ")
    # response should contain 5 digits, representing the LetterInformation enum.
    # PRESENT = 2  # yellow
    # NOT_PRESENT = 3 # dark grey
    # CORRECT = 4  # green
    # The correct word would result in '44444'

    result = input()
    if result == "" or result == '44444':
        print("Success!")
        break
    info = []
    for i in range(5):
        info.append(LetterInformation(int(result[i])))
    guess_history.append((guess, info))
    attempts += 1
