"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
import random
from statistics import mean, mode, median

attempt_list = []

# I have no specific reason for why I made these two variables,
# other than trying to clean up the look of start game function.
low_guess = "Too low, try again."
high_guess = "Too high, try again."

#the menu options prompt
def menu():
    print("+++ Number Guessing Game Menu +++")
    print("""Options:
    Enter 'HELP' for game instructions
    Enter 'PLAY' to begin the game
    Enter 'EXIT' to exit the program
    """)

#game stats following completion of the game
def stats():
    print(f"""[Best score: {min(attempt_list)}]
    This game took {attempt_list[-1]} attempts.
    The average of all scores is {mean(attempt_list)}.
    The median of all scores is {median(attempt_list)}.
    The mode of all scores is {mode(attempt_list)}.
    """)

# start menu option    
def show_help():
    print("[Instructions: Guess a number between 1 and 10. Your lowest number of attempts is your highscore!]")

# game function, errors and exceptions
def start_game():
    play_again = 'y'
    while play_again.lower() == 'y':
        solution = random.randint(1,10)
        print("***** Welcome to the Number Guessing Game! *****")
        user_guess = input("Enter your guess: ")
        tries = 1
        try:
            user_guess = int(user_guess)
            if user_guess > 10:
                raise ValueError()
                continue
            elif user_guess < 1:
                raise ValueError()
                continue
            while user_guess != solution:
                print(f"[Attempt: {tries}]")
                if int(user_guess) < solution:
                    tries += 1
                    print(low_guess)
                    user_guess = int(input("Your guess: "))
                elif int(user_guess) > solution:
                    tries += 1
                    print (high_guess)
                    user_guess = int(input("Your guess: "))
            else:
                print("Got it! Great job.")
                attempt_list.append(tries)
                print(f"[Your score: {tries}]")
                stats()
        except ValueError:
            print("HEY! That's not a valid integer. Please try again.")
            continue
        play_again = input("Would you like to play again? (y/n): ")
    else:
        print("Thanks for playing! Here are your finishing stats:")
        print(f"[Your score: {tries}]")
        stats()

# Lastly, calling the code to run in this order:
menu()
while True:
    user_choice = input("What would you like to do? -> ")
    if user_choice.lower() == 'exit':
        break
    elif user_choice.lower() == 'help':
        show_help()
        continue
    elif user_choice.lower() == 'play':
        start_game()
        break


# Trying to work out some error issues: 
# 1) Why are some of my errors are passive? For example: if I guess an integer within range on my first attempt everything works fine. But say I guess an out-of-range integer for my second attempt, it will not raise an error (FYI: if i guess out-of-range on my first attempt, it WILL raise an error). I'm sure there is some issue in my order of things.
# 2) my raised errors will restart the game, re-randomizing the number. How do I put it so that it continues to let the user try again within the current game?