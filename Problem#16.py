# Number Guessing Game!

import random
secret = random.randint(1, 100)

has_won = 0
attempt = 0
while attempt < 10:
    guess = int(input("Enter a number between 1 and 100:"))
    attempt += 1
    if 1 <= guess <= 100:
        if guess == secret: 
            print(f"Congrats! You guessed it right in {attempt} attempt.")
            has_won = 1
            break
        elif guess > secret:
            print("Too High! Try again.")
        else:
            print("Too low! Try again.")     
    else :
        print("You have exceed the Range (1-100), Please Try Again!") 
        attempt -= 1 
    print(f"Attempts left: {10 - attempt}") 
if has_won == 0:
    print(f"Game over, The number was {secret}. Better luck! Next time.")




