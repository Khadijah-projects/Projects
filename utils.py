import random

easy= {"max_num" : 50, "attempt" : 10, "multiplier" : 100}
medium = {"max_num" : 100, "attempt" : 7, "multiplier" : 150}
hard = {"max_num" : 200, "attempt" : 5, "multiplier" : 200}


def input_validator(max_num):
    while True:
        try:
            player_num = int(input("guess a random number: "))
            if player_num >= 1 and player_num <= max_num:
                return player_num
        except:
            print(f"value typed is not a number, the range number is between 1 and {max_num}")
        else:
            print(f"value typed is outside the range number, the range number is between 1 and {max_num}")

def difficulty_selector():
    while True:
        print("\nselect a level")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")  
        level = (input("select your level: "))  
        if level == '1':
            print("I'm thinking of a number between 1 and 50") 
            print("You have 10 attempts")
            return easy
        elif level == '2':
            print("I'm thinking of a number between 1 and 100") 
            print("You have 7 attempts")
            return medium
        elif level == '3':
            print("I'm thinking of a number between 1 and 200") 
            print("You have 5 attempts")
            return hard
        else:
            print("invalid level, the level is between 1, 2 and 3")           
          
def guess_num(max_num, attempt, multiplier):
    secret_num = random.randint(1, max_num)
    for j in range(attempt):
        attempt_used = j + 1
        player_num = input_validator(max_num)
        if secret_num == player_num:
            print("you won")
            scores = (attempt - attempt_used +1)*multiplier
            print(f"You score {scores} in {attempt_used} attempt")
            break
        elif player_num < secret_num:
            print("guess a higher number")
        else:
            print("guess a lower number")
        if j == attempt_used:
            print(f"you lose, this is the secret number {secret_num}")
    else:
        print(f"You lose! The secret number was {secret_num}")
        print(f"You used all {attempt} attempts")

