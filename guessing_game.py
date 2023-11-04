"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# Grade Expectation:
# I am aiming for an exceeds expectation grade. 
# If the game does not meet those standards, please reject so that I may correct the errors.

import random
from statistics import mean, mode, median

attempt_list = []

# the menu options prompt
def menu():
    print("***** WELCOME TO THE NUMBER GUESSING GAME *****")
    print("""
    MENU:
        Enter 'HELP' for game instructions
        Enter 'PLAY' to begin the game
        Enter 'EXIT' to exit the program
    """)

# game stats following completion of the game
def stats():
    print(f"""STATS:
    [Highscore: {min(attempt_list)}]
    * Your last game used {attempt_list[-1]} attempts.
    * The average of all game scores is {mean(attempt_list)}.
    * The median of all game scores is {median(attempt_list)}.
    * The mode of all game scores is {mode(attempt_list)}.
    """)

# start menu (help) option    
def show_help():
    print("""
    Instructions:
        In this game, you will guess a whole number, between 1 and 100.
        Your aim is to blindly guess the answer that the program has generated.
        Try to use the least number of attempts as possible (1 attempt being the best).
        Lowest number of attempts = highest score
        
        *Type 'EXIT' to quit game program.*
        *Type 'PLAY' to start game.*
    """)

# game function
def start_game():
    tries = 0
    solution = random.randint(1,100)
    print("\n[Highscore: 0]")
    print("++++ Ready, Set, Go! ++++\n")
    while True:
        try:
            user_guess = input("Enter your guess: ")
            if user_guess.lower() == 'exit':
                break
            elif int(user_guess) > 100:
                tries += 1
                raise Exception("Error: Need an integer between 1 and 100. Try again.\n")
                continue
            elif int(user_guess) < 1:
                tries += 1
                raise Exception("Error: Need an integer between 1 and 100. Try again.\n")
                continue
            elif int(user_guess) < solution:
                tries += 1
                print("It's higher, try again.\n")
                continue
            elif int(user_guess) > solution:
                tries += 1
                print ("It's lower, try again.\n")
                continue
            else:
                tries += 1
                print("Got it! Great job.")
                attempt_list.append(tries)
                print(f"[Your attempt score: {tries}]")
        except ValueError as err:
            print("ERROR: That's not an integer. Please try again.")
            continue
        except Exception as err:
            print(err)
            continue
        # asks the user if they'd like to play again and what to do if 'yes'(y).
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == 'y':
            tries = 0 
            solution = random.randint(1,100)
            print(f"[Highscore: {min(attempt_list)}]")
            print("""++++ Ready, Set, Go! ++++\n""")
            continue
        else:
            print(f"""
            Until next time, Goodbye!
            """)
            stats()
            break

# calling the code to run in this order:
menu()
while True:
    user_choice = input("WHAT DO YOU WANT TO DO? > ")
    if user_choice.lower() == 'exit':
        break
    elif user_choice.lower() == 'help':
        show_help()
        continue
    elif user_choice.lower() == 'play':
        start_game()
        break