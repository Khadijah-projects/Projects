from utils import difficulty_selector, guess_num
print("WELCOME TO THE NUMBER GUESSING GAME")
level = difficulty_selector()

if level:

    max_num = level["max_num"]
    attempt = level["attempt"]
    multiplier = level["multiplier"]

    guess_num(max_num, attempt, multiplier)