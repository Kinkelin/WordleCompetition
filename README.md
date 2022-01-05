# Wordle AI Competition
This is the draft version of the repository for a Wordle AI Competition. AIs will try to become the optimal https://www.powerlanguage.co.uk/wordle/ wordle player.
The actual competition will maybe run monthly? with previously submitted AIs trying to guess the official words of the month. A number of unofficial word lists are in this repository for testing purposes.

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

# Run the test competition
- Run competition.py. By default 2 divisions are run with 1000 random words each:
- Normal: All AIs in ai_implementations will compete.
- Hard Mode: All AIs in ai_implementations_hard_mode will compete.
- You can pass true for the print_details argument in the Competition.fight calls in the main method if you want to see guesses and scoring.

# How to implement your own AI
Inherit from the abstract WordleAI class and implement it's guess method. See the Monkey AI classes for an example implementation. You can find detailed documentation about this interface in the WordleAI class itself.

# Official wordle word list
The exact word list is not public. The following is known (according to Wikipedia): Each daily game uses a randomly selected word from a list of 2,500 words. The developer has said that he does not know the day's word so can still enjoy playing the game himself.

# Data
In the data folder a few unofficial word lists can be found:
- wordle historic words: A few words that appeared as official wordles. Data from reddit. Please help out if you know more words!
- word list https://github.com/dwyl/english-words: List of > 450k English words
- word list from http://mieliestronk.com/corncob-lowercase.txt: List of > 58k English words
- From https://github.com/first20hours/google-10000-english: Lists of the 10000 most common English words in order of frequency
- Common words from ef.com: Top 3000 and 1000 most common English words, alphabetically sorted
- A list of 750 words of Basic English from https://en.wikipedia.org/wiki/Basic_English