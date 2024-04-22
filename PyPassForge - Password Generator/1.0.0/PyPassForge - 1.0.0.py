### 2024 Alejandro Romeo

import random
import os

def clear():
    os.system('cls')

def main():
    alphanumeric = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", 
    "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", 
    "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", ",", 
    ".", "<", ">", "/", "?"
    ]

    pwd = ""
    # Welcome
    clear()
    print("--------------------------------------\nPyPassForge 1.0.0 - By Alejandro Romeo\n--------------------------------------\n")

    while True:
        # Password lenght error loop
        while True:
            try:
                lenght = int(input("Please, enter the lenght of the password to generate [12 - 24]: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number!")
        
        # Lenght check
        if lenght < 12 or lenght > 24:
            print("Invalid input, Please enter a valid number!")
            continue
        break

    clear()
    print('Press ENTER to regenerate the password or "q" to quit')
    # Infinite password generator
    while True:
        # Generate and add each character
        for i in range(lenght):
            rand_char = random.choice(alphanumeric)
            pwd += rand_char
        user_input = input(pwd)
        # Quit check
        if user_input == "q":
            quit()
        pwd = ""

if __name__ == "__main__":
    main()