# WordleCompetition
This is the draft version of the repository for a Wordle AI Competition. AIs will try to become the optimal https://www.powerlanguage.co.uk/wordle/ wordle player.

# Rules
- In each round of wordle you try to guess a 5 letter long word
- You have 6 guesses
- After each guess you will receive information about which letters of your guess were correct
- The goal is to collect as few points as possible. A round will gives points equal the number of guesses or 10 points if the word was not found within the 6 guesses.
- The winner of a competition is the competitor with the least amount of points over all the rounds.

# Run the competition
Run competition.py. By default 2 divisions are run with 1000 random words each:
Normal: All AIs in ai_implementations will compete.
Hard Mode: All AIs in ai_implementations_hard_mode will compete with the Wordle Hard Mode rules.

You can pass true for the print_details argument in the Competition.fight calls in the main method if you want to see guesses and scoring.

# How to implement your own AI
Inherit from the abstract WordleAI class and implement it's guess method. See the Monkey AI classes for an example implementation. You can find detailed documentation about this interface in the WordleAI class itself.


