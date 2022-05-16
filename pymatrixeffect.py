from time import sleep
import colorama as clr
import platform
import random
import os

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    # Initialize colorama when OS is Windows
    if platform.system() == "Windows":
        clr.init()

    # Set Matrix characters
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':,./<>?"

    # Clear the screen
    clear()

    # Get the current terminal size
    lines = os.get_terminal_size().lines
    columns = os.get_terminal_size().columns

    # Set background color to black
    for i in range(lines * columns):
        print(clr.Back.BLACK + " ", end = "")


    # Randomly print characters
    try:
        while True:
            for character in characters:
                randnum = random.randint(1, 10)

                if randnum <= 5:
                    print(clr.Back.BLACK + clr.Fore.GREEN + character, end = "")
                else:
                    print(clr.Back.BLACK + clr.Fore.GREEN + " ", end = "")

                sleep(.005)
    except KeyboardInterrupt:
        # Gracefully exit when Ctrl+C is pressed
        clear()
        exit()

    