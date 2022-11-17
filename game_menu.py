"""
basic python code - 16/11/22 - Glauber Cavalcante
"""

import os
import sys
import guess
import hangman

def display_menu(menu):

    for i in range(1,3):
        for x in range(1,26):    print("*",end="")
        if(i == 1):    print("\npy Games - Choose it now! ")
    print("")

    for k, function in menu.items():
        print(k, function.__name__)

def hangman_game():
    hangman.play()

def guess_the_number():
    guess.play()

def exit_game():
    sys.exit()

def clear_screen():
    clear = lambda: os.system('cls')
    clear()

def main():
    clear_screen()
    functions_names = [hangman_game, guess_the_number, exit_game]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Please enter the number of your game: "))  # Get function key

        clear_screen()
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function

if __name__ == "__main__":
    main()