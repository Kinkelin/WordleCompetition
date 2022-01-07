# Wordle AI Competition
In this repository you can find everything you need to hold [Wordle](https://www.powerlanguage.co.uk/wordle/) AI competitions. Implement and test your own AIs to find the optimal wordle strategy!

# How to implement your own AI
Inherit from the abstract [WordleAI](WordleAI.py) class and implement its `guess()` method. See the [Monkey AI](ai_implementations/MonkeyAI.py) classes for an example implementation. You can find detailed documentation about this interface in the WordleAI class itself.

# Run the test competition
- Run [Competition.py](Competition.py). By default, 2 divisions are run with 1000 random words each:
- Normal: All AIs in ai_implementations will compete.
- Hard Mode: All AIs in ai_implementations_hard_mode will compete.
- You can pass `True` for the `print_details` argument in the `Competition.fight()` calls in the main method if you want to see guesses and scoring.

# Wordle rules
- In each round of wordle you try to guess a random 5 letter word
- Words only contain letters a-z and are lower case.
- You have 6 guesses
- After each guess you will receive information about which letters of your guess were correct

# AI Competition rules 
- The goal is to collect as few points as possible. A round gives points equal the number of guesses or 10 points if the word was not found within the 6 guesses.
- The winner of a competition is the competitor with the least amount of points over all rounds combined.

# Hard Mode rules
- Standard rules apply
- Guesses must follow already known information. Revealed letters have to be part of the guess, if possible at the right position.

# Official wordle word list
The word list of the official wordle game consists of 12972 words: [combined_wordlist.txt](data/official/combined_wordlist.txt)<br>
Around 2500 of them are used as the daily wordles: [shuffled_real_wordles.txt](data/official/shuffled_real_wordles.txt).

# Unofficial word lists
In the data folder a few unofficial word lists can be found:
- word list https://github.com/dwyl/english-words: List of > 450k English words
- word list from http://mieliestronk.com/corncob-lowercase.txt: List of > 58k English words
- From https://github.com/first20hours/google-10000-english: Lists of the 10000 most common English words in order of frequency
- Common words from ef.com: Top 3000 and 1000 most common English words, alphabetically sorted
- A list of 750 words of Basic English from https://en.wikipedia.org/wiki/Basic_English