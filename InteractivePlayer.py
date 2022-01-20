from WordList import WordList
from WordleAI import LetterInformation
from ai_implementations.LetterPopularityAI import LetterPopularityAI

"""
Executing this file allows playing the game in the browser with AI support. Simply relay the ingame information 
to the AI via console input. 
For each guess a 5-character response is expected, with either letters or digits representing LetterInformation:
PRESENT = 2 or p      # yellow
NOT_PRESENT = 3 or n # dark grey
CORRECT = 4 or c      # green

A 100% correct guess would result in:
44444 
or 
ccccc

Assign your AI to the ai variable.
List already done guesses in the guesses variable.

"""

def to_enum(char):
    if char.isdigit():
        return int(char)
    if char == 'c':
        return 4
    if char == 'p':
        return 2
    return 3

ai = LetterPopularityAI(WordList("data/official/combined_wordlist.txt").get_list_copy())
guesses = [] # pass already done guesses in this list. It will overwrite the first AI guesses. You still have to relay the responses through console input

attempts = 0
guess_history = []
while attempts < 6:
    guess = ai.guess(guess_history)
    if attempts < len(guesses):
        guess = guesses[attempts]
    print("AI guesses ", guess)
    print("Please type a response: ")
    result = input()
    if result == "" or result == '44444' or result == 'ccccc':
        print("Success!")
        break
    info = []
    for i in range(5):
        info.append(LetterInformation(to_enum(result[i])))
    guess_history.append((guess, info))
    attempts += 1
