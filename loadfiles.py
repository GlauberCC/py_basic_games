"""
basic python code - 16/11/22 - Glauber Cavalcante
"""

def play():
    file_hangman = open("hangman_file.txt","w")
    file_hangman.write("banana\n")
    file_hangman.write("watermelon\n")
    file_hangman.write("grape\n")
    file_hangman.close()


if(__name__ == "__main__"):
    play()