"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
import random
from statistics import mean, mode, median

attempt_list = []

#the menu options prompt
def menu():
    print("***** WELCOME TO THE NUMBER GUESSING GAME *****")
    print("""
    MENU:
        Enter 'HELP' for game instructions
        Enter 'PLAY' to begin the game
        Enter 'EXIT' to exit the program
    """)

#game stats following completion of the game
def stats():
    print(f"""STATS:
    [Best attempt score: {min(attempt_list)}]
    * Your last game used {attempt_list[-1]} attempts.
    * The average of all game scores is {mean(attempt_list)}.
    * The median of all game scores is {median(attempt_list)}.
    * The mode of all game scores is {mode(attempt_list)}.
    """)

# start menu option    
def show_help():
    print("""
    Instructions:
        Guess a number between 1 and 10.
        Try to get the lowest number of attempts possible!
    """)

# game function
def start_game():
    tries = 0
    solution = random.randint(1,10)
    print("++++ Ready, Set, Go! ++++")
    print("solution = ", solution) # DELETE THIS LINE
    while True:
        try:
            user_guess = input("Enter your guess: ")
            if int(user_guess) > 10:
                tries += 1
                raise ValueError("OOPS!: Please use an integer between 1 and 10.")
                continue
            elif int(user_guess) < 1:
                tries += 1
                raise ValueError("OOPS!: Please use an integer between 1 and 10.")
                continue
            elif int(user_guess) < solution:
                tries += 1
                print("Too low, try again.")
                continue
            elif int(user_guess) > solution:
                tries += 1
                print ("Too high, try again.")
                continue
            else:
                tries += 1
                print("Got it! Great job.")
                attempt_list.append(tries)
                print(f"[Your attempt score: {tries}]")
        except ValueError as err:
            print("ERROR: That's not an integer. Please try again.")
            continue
        play_again = input("Would you like to play again? (y/n): ") # "play again?" prompt
        if play_again.lower() == 'y':
            tries = 0 
            solution = random.randint(1,10)
            print("""
            ***** Ready, Set, Go! *****""")
            print("solution = ", solution) # DELETE THIS LINE
            continue
        else:
            print(f"""
            Until next time, Goodbye!
            """)
            stats()
            break

# Lastly, calling the code to run in this order:
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
        
# DON'T FORGET: Delete lines revealing the solution (line 49, line 83)