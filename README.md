# Wordle AI Competition
In this repository you can find everything you need to hold [Wordle](https://www.powerlanguage.co.uk/wordle/) AI competitions. Implement and test your own AIs to find the optimal wordle strategy!

# Leaderboard

| Nr | AI                 | Author    | Points per round | Success rate |
|----|--------------------|-----------|------------------|--------------|
| 1  | LetterPopularityAI | da Finnci | 4.911            | 91.4%        |
| 2  | MonkeyAI           | da Finnci | 9.995            | 0.1%         |

The leaderboard shows how AIs contained in this repository perform against offical wordles, 
using the first 1000 words found [here](data/official/shuffled_real_wordles.txt). 

You can submit your own implementation by creating a pull request or sending it to me directly. 
The leaderboard will be updated accordingly.

AIs should use the word list provided in the constructor call and must not use the official wordle list directly. 
It is allowed (and encouraged) to use a common words list to mimic inherint human knowledge. 
See [WordleJudge](#wordlejudgepy) for details. 

# How to implement your own AI
Inherit from the abstract [WordleAI](WordleAI.py) class and implement its `guess()` method. 
You can find detailed documentation about this interface in the WordleAI class itself.

See the [Monkey AI](ai_implementations/MonkeyAI.py) and [LetterPopularityAI](ai_implementations/LetterPopularityAI.py) classes for example implementations. 
Feel free to reuse any code in your own implementations, for example the `remaining_options()` method.

# Run the test competition
- Run [Competition.py](Competition.py). 
- By default, the same configuration is run that is used for the Leaderboard. 
All AIs found in [ai_implementations](ai_implementations) will compete for 1000 [wordles](data/official/shuffled_real_wordles.txt). 
Hard mode is not enforced.
- You can pass `True` for the `print_details` argument in the `Competition.fight()` calls in the main method if you want to see guesses and scoring by round.

# Community
Feel free to hop onto our [Discord](https://discord.gg/BxVpFXne) to discuss strategy, 
ask for help or boast about your AI's playing strength!

# Wordle rules
- In each round of wordle you try to guess a random 5-letter word
- Words only contain letters a-z and are lower case.
- You have 6 guesses
- After each guess you will receive information about which letters of your guess were correct

# AI Competition rules 
- The goal is to collect as few points as possible. A round gives points equal the number of guesses or 10 points if the word was not found within the 6 guesses.
- The winner of a competition is the competitor with the least amount of points over all rounds combined.

# InteractivePlayer.py
Executing this file allows playing the game in the browser with AI support. Simply relay the ingame information
to the AI via console input.

# WordleJudge.py
Helper class to take into account how common words are in the English language. 
Use an instance of this class and call `is_wordle_probability(word)` to factor word usage frequency into your decision making.

# Hard Mode rules
This is an optional setting in the official game.
- Standard rules apply
- Guesses must follow already known information. Revealed letters have to be part of the guess, if possible at the right position.

# Official wordle word list
The word list of the official wordle game consists of 12972 words: [combined_wordlist.txt](data/official/combined_wordlist.txt)<br>
Around 2500 of them are used as the daily wordles: [shuffled_real_wordles.txt](data/official/shuffled_real_wordles.txt).

# Unofficial word lists
In the data folder a few unofficial word lists can be found:
- from https://gist.github.com/h3xx/1976236: List of 100k English words ordered by usage frequency
- from https://github.com/dwyl/english-words: List of > 450k English words ordered alphabetically
- from http://mieliestronk.com/corncob-lowercase.txt: List of > 58k English words ordered alphabetically
- from https://github.com/first20hours/google-10000-english: Lists of 10k common English words ordered by usage frequency
- from ef.com: Top 3000 and 1000 most common English words, alphabetically sorted
- A list of 750 words of Basic English from https://en.wikipedia.org/wiki/Basic_English