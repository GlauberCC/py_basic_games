"""
basic python code - 16/11/22 - Glauber Cavalcante
"""

import os
import random
import hangman
import game_menu

def play():
    print_title()
    secret_word = load_secret_word()

    correct_characteres = load_correct_characters(secret_word)

    errors = 0
    hanged = False
    correct = False
    wrong_guess_list = []

    while(not hanged and not correct):
        attempts = 6-errors
        guess = request_guess(attempts)

        if(guess in secret_word):
            if (len(guess) > 1):
                correct = secret_word == guess
                if(correct):
                    print_won_message(secret_word)
                    break
                else:
                    errors += 1
                    desenha_forca(errors, correct_characteres)

            if (guess in correct_characteres):
                print("[-- You already used this guess before --]")

            correct_characteres = set_correct_guess(secret_word, guess, correct_characteres)
        else:
            wrong_guess_list.append(guess)
            errors += 1
            desenha_forca(errors, wrong_guess_list)

        correct = "_" not in correct_characteres
        hanged = errors == 6
        print(correct_characteres)
    if(correct):
        print_won_message(secret_word)
    else:
        print_lose_message(secret_word)
    set_menu()

def print_title():
    clear_screen()
    for i in range(1,3):
        for x in range(1,28):
            print("*",end="")
        if(i == 1):
            print("\nWelcome to the Hangman game")
    print("")

def load_secret_word():
    words_list = []
    with open("hangman_file.txt","r") as file:
        for line in file:
            words_list.append(line.upper().strip())

    return words_list[random.randrange(0,len(words_list))]

def load_correct_characters(str_secret_word):
    str_correct_characteres = ["_" for character in str_secret_word] #List Comprehensions
    print(str_correct_characteres)
    return str_correct_characteres

def request_guess(attempts):
    print("You still have {} attempts".format(attempts))
    guess = input("Choose one character: ")
    return guess.upper().strip()

def print_won_message(str_secret_word):
    print("CORRECT! YOU WON! {}".format(str_secret_word))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("")

def print_lose_message(str_secret_word):
    print("YOU LOSE! .. the word was: {}".format(str_secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("")

def set_correct_guess(str_secret_word, str_guess, str_correct_characteres):
    index = 0
    for character in str_secret_word:
        if (str_guess == character):
            str_correct_characteres[index] = character
        index = index + 1
    return str_correct_characteres

def desenha_forca(erros, wrong_guess_list):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         wrong words: {}".format(wrong_guess_list))
    print()

def play_again():
    hangman.play()

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

def clear_screen():
    clear = lambda: os.system('cls')
    clear()

if(__name__ == "__main__"):
    play()

