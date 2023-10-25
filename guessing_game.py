"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
import random
from statistics import mean, mode, median

solution = random.randint(1,10)
attempt_list = []

# create a function for the game, help, and play again function
def menu():
    print("+++ Number Guessing Game Menu +++")
    print("""
    Enter 'HELP' for game instructions
    Enter 'PLAY' to begin the game
    Enter 'EXIT' to exit the program
    """)
def stats():
    print(f"[Highscore: {min(attempt_list)}]")
    print(f"""
    The average of all scores is {mean(attempt_list)}.
    The median of all scores is {median(attempt_list)}.
    The mode of all scores is {mode(attempt_list)}.
    """)
    
def show_help():
    print("**Guess a number between 1 and 10. Your lowest number of attempts is your highscore!**")

def start_game():
    play_again = 'y'
    while play_again.lower() == 'y':
        solution = random.randint(1,10)
        print("***** Welcome to the Number Guessing Game! *****")
        user_guess = int(input("Enter your guess: "))
        tries = 1
        while user_guess != solution:
            print(f"[Total attempts: {tries}]") #new
            
            if user_guess < solution:
                tries += 1
                user_guess = int(input("Too low. Try again: "))
            elif user_guess > solution:
                tries += 1
                user_guess = int(input("Too high. Try again: "))
        else:
            print("Got it! Great job.")
            attempt_list.append(tries) #new
            print(f"[Your score: {tries}]")
            stats()
            play_again = input("Would you like to play again? (y/n): ")
    else:
        print("Thanks for playing! Here are your finishing stats:")
        print(f"[Your score: {tries}]")
        stats()
        
    menu()
    
menu()
while True:
    user_choice = input("What would you like to do? -> ")
    if user_choice.lower() == 'exit':
        break
    elif user_choice.lower() == 'help':
        show_help()
        continue
    elif user_choice.lower() == 'play':
        play_again = 'y'
        start_game()
        break


#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.
# ( You can add more features/enhancements if you'd like to. )
# Kick off the program by calling the start_game function.