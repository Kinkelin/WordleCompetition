# Wordle AI Competition
In this repository you can find everything you need to hold [Wordle](https://www.powerlanguage.co.uk/wordle/) AI competitions. Implement and test your own AIs to find the optimal wordle strategy!

# Leaderboard
|Nr |        AI        | Author  |Points per round|Success rate|
|---|------------------|---------|----------------|------------|
|1  |OutcomeBasedAI    |da Finnci|3.816           |100.0%      |
|2  |RubzipAI          |rubzip  |4.583           |96.9%       |
|3  |LetterPopularityAI|example  |4.653           |93.6%       |
|4  |BruugleAI         |Bruugle  |6.120           |97.0%       |
|5  |MonkeyAI          |example  |9.986           |0.2%        |

The leaderboard shows how AIs contained in this repository perform against offical wordles, 
using the first 1000 words found [here](data/official/shuffled_real_wordles.txt). 

You can submit your own implementation by creating a pull request or sending it to me directly. 
The leaderboard will be updated accordingly.

AIs should use the word list [provided](data/official/combined_wordlist.txt) in the constructor call and must not use the [solution](data/official/shuffled_real_wordles.txt) list directly. 
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

# Word lists
The word list of the official wordle game consists of 12972 words: [combined_wordlist.txt](data/official/combined_wordlist.txt)<br>
Around 2500 of them are used as the daily wordles: [shuffled_real_wordles.txt](data/official/shuffled_real_wordles.txt)<br>

In this repository is also a list of 5-letter English words ordered by usage frequency [common_words.txt](data/other/common_words.txt) that was extracted from a [wictionary.org](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/PG/2005/08/1-10000) list of 100k common words.

Also a list with words that are difficult for AIs to solve can be found under [difficult_words.txt](data/other/difficult_words.txt) for testing purposes.

# WordleJudge.py
Analysis has shown that the daily wordles are significantly more frequently used words than the average allowed-guess word. 
This is something human players automatically adjust for - they are more likely to guess 'water' than 'pekoe' (a specific tea). 

The WordleJudge class takes into account how common words are in the English language. 
Use an instance of this class and call `is_wordle_probability(word)` to factor word usage frequency into your decision-making.


# Hard Mode rules
This is an optional setting in the official game.
- Standard rules apply
- Guesses must follow already known information. Revealed letters have to be part of the guess, if possible at the right position.
