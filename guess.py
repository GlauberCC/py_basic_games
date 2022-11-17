"""
basic python code - 16/11/22 - Glauber Cavalcante
"""

import os
import random
import game_menu
import guess

def play():
    print_title()

    #variables
    secret_number = random.randrange(1,101) #print("random = {}".format(secret_number))
    score = 1000
    round = 1

    attempt_total = choose_level()

    while(round <= attempt_total):
        print("Attempt: {} de {}".format(round, attempt_total))
        guess_str = input("Type the guess number: ")
        guess = int(guess_str)

        if(guess < 1) or (guess > 100):
            print("You must to type a number between 1 and 100!")
            continue

        if (validate_the_guess(secret_number, guess)):
            break

        score = score - (1000/attempt_total)

    print("\nEnd of Game - Secret Number = {}".format(secret_number))
    print("Final Score = {}".format(score))
    set_menu()

def print_title():
    clear_screen()
    for i in range(1, 3):
        for x in range(1, 26):    print("*", end="")
        if (i == 1):    print("\nWelcome to the Guess game")
    print("")

def clear_screen():
    clear = lambda: os.system('cls')
    clear()

def choose_level():
    print("Level?: (1) Easy | (2) Medium | (3) Hard")
    level = int(input("Choose the level: "))
    if (level == 1):
        int_attempt_total = 20
    elif (level == 2):
        int_attempt_total = 10
    else:
        int_attempt_total = 5
    return int_attempt_total

def validate_the_guess(int_secret_number, int_guess):
    correct = int_secret_number == int_guess
    higher = int_guess > int_secret_number
    lower = int_guess < int_secret_number

    if correct:
        print("You won !!! ")
    else:
        if (higher):
            print("Wrong, your number is higher")
        elif (lower):
            print("Wrong, your number is Lower")
    return correct

def play_again():
    guess.play()

def back_to_menu():
    game_menu.main()

def close():
    print("Thank you for playing!")
    exit()

def display_menu(menu):
    for k, function in menu.items():
        print(k, function.__name__)

def set_menu():
    functions_names = [play_again, back_to_menu, close]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Now you choose one option: (1) play_again (2) back_to_menu (3) close "))

        selected_value = menu_items[selection]
        selected_value()

if(__name__ == "__main__"):
    play()

    # "$ {:7:2f}".format(1.5) = 7 spaces + 2 decimal
    # "$ {:07:2f}".format(1.5) = 7 zeros/spaces + 2 decimal
    # "$ {:07d}".format(1.5) = 7 zeros/int + 2 decimal
    # "Data {:02d}/{:02d}".format(19.11) = Data 19/11
    # https://docs.python.org/3/library/string.html#formatexamples

    #buit-in Documentation https://docs.python.org/3/library/functions.html
    # 3 // 2 = 1 = Interdivision operator, return int without round it