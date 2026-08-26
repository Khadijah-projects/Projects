This is a simple number guessing game that we built with Python. It allows the computer to generate a random number, and the player tries to guess the number. This game has 3 difficulty levels: Easy (1–50, with 10 attempts), Medium (1–100, with 7 attempts), and Hard (1–200, with 5 attempts).

We created 2 files for this project, which are utils.py and game.py. The utils.py contains the main functions:

difficulty_selector: This allows the player to choose a difficulty level.

input_validator: This checks if the number the player chose is a valid number between the selected range.

guess_number: This is used to run the main guessing game.

random.randint(): is used to generate the secret number.

We also used dictionaries to store the settings for each level. So, once the player enters their guess, the game tells the player to guess either a lower or higher number. If the player guesses correctly, it will say "you won." The player also gets a score depending on how early they guess the right number. If the player uses all their attempts without guessing correctly, they lose, and the secret number is revealed.

The game.py is the main file used to run the game. We imported the difficulty_selector and guess_number functions from utils.py. So, after the player chooses a level, we get the max_num, number of attempts and multiplier from the dictionary. We then input these values into the guess_number function and the game starts running.
