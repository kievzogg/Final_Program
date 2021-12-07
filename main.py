"""
_author_
Kiev Zogg
_date_
9/23/2021

A program that does an assortment of actions including
calculations with numbers, having the use guess number as well
as a program that created a randomly sized rectangle.
"""

# Imports
from random import randrange


# Calculation Method
def calc():
    """
Calculation Method. Receives two numbers from user and performs a number
of calculations on them
    """
    # Variables
    num1 = 0
    num2 = 0
    # Program loop
    # Boolean Program Loop
    run_program = True

    # While loop that executes until Boolean is False
    while run_program:

        print("\n\n--Calculations--")

        # Number inputs
        # Error handling via Try/Except
        while True:
            try:
                num1 = float(input("Enter first number: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            else:
                break
        while True:
            try:
                num2 = float(input("Enter a second number: "))
            except ValueError:
                print("Please enter a valid integer")
                continue
            else:
                break

        # Error handling

        # Calculations
        # Addition
        print(num1, " + ", num2, " = ", num1 + num2)
        # Subtraction
        print(num1, " - ", num2, " = ", num1 - num2)
        # Division
        print(num1, " / ", num2, " = ", num1 / num2)
        # Power of
        print(num1, " to the power of ", num2, " = ", num1 ** num2)
        # Retuns remainder
        print(num1, " % ", num2, " = ", num1 % num2)
        # Floor Division
        print(num1, " // ", num2, " = ", format(num1 // num2, ".0f"))

        # Asks user if they would like to run calculations with new numbers
        run_program_bool = input("\nRun program again? (y/n)")

        # If/Else statement that turns the Loop Boolean False if the answer is
        # anything but "y"
        if run_program_bool.lower() == "n":
            run_program = False
        elif run_program_bool.lower() != "y":
            # Handles unexpected input / Reverts to Menu Screen menu()
            print("Unexpected answer! Reverting to Menu Screen")
            run_program = False
            menu()


# Number Guesser Method
def num_guesser():
    """
Has the user guess a randomly generated integer within 4 tries
    """

    # Variables
    user_guess = 0
    # Print Message to User
    print("\nGuess a number 0-20 within 4 tries!")
    # Assigns Random Number
    random_int = randrange(21)

    false_guess = True
    num_of_guesses = 0

    # Loop that runs until Guesses are used up or correct answer is choosen
    while false_guess and not (num_of_guesses == 4):
        # User Guess
        while True:
            try:
                user_guess = int(input("Your Guess: "))
            except ValueError:
                print("Please enter a whole number")
                continue
            else:
                break
        # Correct Guess
        if user_guess == random_int:
            false_guess = False
            print("Congratulations you guessed the correct number!")
        # High Guess
        elif user_guess > random_int:
            num_of_guesses += 1
            print("You guessed to high\nYou have", 4 - num_of_guesses,
                  "remaining.")
        # Low Guess
        elif user_guess < random_int:
            num_of_guesses += 1
            print("You guessed to low\nYou have", 4 - num_of_guesses,
                  "remaining.")
        # Informs user if they run out of guesses
        if num_of_guesses == 4:
            print("\nYou are out of guesses. The number was", random_int)
    # Returns to menu screen
    menu()


# Method that print a random rectangle to the screen
def fun_method(row, column):
    """
Generates a rectangular box of hashtags via random integers
Also prints BOO if row or column are equal to 4
    :param row: Random Integer
    :param column: Random Integer
    """
    # Rows
    for x in range(row):
        # Columns
        for y in range(column):
            print("#", sep="", end="")
        print("")
    # Spooky Surprise, if either the row or column equal 4 BOO is printed
    if (row or column) == 4:
        print("BOOO")
    # Calls menu
    user_input()


# Menu Method
def menu():
    """
Prints menu/commands to screen
    """
    # Prints UI to Screen
    print("\n--Welcome to Numbers Fun", end="--\n")
    print("|Type the respective letter in parentheses to SELECT|")
    print("Programs")
    print("-Calculations (s)")
    print("-Number Guesser (n)")
    print("-Fun Surprise (f)")
    print("-Close program(c)", end="\n\n")

    user_input()


def user_input():
    """
Controls the main User Input for the main menu
    """
    # Command
    command = input("Enter command: ")

    # S = Starts program
    # C = Close program
    if command.lower() == "s":
        print("Starting Calculations\n")
        calc()
    elif command.lower() == "n":
        print("Starting Number Guesser")
        num_guesser()
    elif command.lower() == "f":
        print("SUPRISE LOADING...")
        fun_method(randrange(7), randrange(20))
    elif command.lower() == "c":
        print("Closing program\n")
        # Prints Bye 3 Times
        print("Bye" * 3, command, sep="")
    else:
        error_handling("(s) (n) (f) (c)")


def error_handling(error):
    """
Handles error from methods in file
    :param error: Commands that must be used
    """
    print("Invalid command!")
    print("Please use given command", error)
    user_input()


# Call menu function
menu()
