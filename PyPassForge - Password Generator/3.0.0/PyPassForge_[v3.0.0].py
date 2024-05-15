import random
import string
import os

# TERMINAL COLORS
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[94m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'
RESET = '\033[0m'

# CHARACTER's TYPES 
abc = string.ascii_lowercase
ABC = string.ascii_uppercase
num = string.digits
sym = string.punctuation

# CHARACTER's TYPES STATUS
char_status = [1, 1, 1, 1]

# PASSWORD GENERATION RESOURCES
pwd_lenght = 12
removal_list = ""
output = f"{WHITE}WELCOME!"

def clear_terminal():
    os.system('cls')

# PRINT UI SECTIONS
def print_ui(section):
    if section == "title":
        print(f"{MAGENTA}•--------------------------------------•\n PyPassForge 3.0.0 - By Alejandro Romeo\n•--------------------------------------•{RESET}")
    if section == "instructions":
        print("\n Press ENTER to generate a password")

# PRINT PARAMETER's STATUS
def print_parameters():
    global char_status
    char_types = ["abc", "ABC", "123", "#$&"]
    print(" ", end = "")
    for type in range(len(char_types)):
        print(f"{char_types[type]}: ", end = "")
        if char_status[type] == 1:
            print(f"{GREEN}ON{RESET}", end = "   ")
        else:
            print(f"{RED}OFF{RESET}", end = "  ")
    print("")

# PRINT OUTPUT LINE
def print_output(output):
    print(f" {YELLOW}[{RESET}",output,f"{YELLOW}]{RESET}", end = " ")

# PASSWORD GENERATOR FUNCTION
def generate_password():
    global char_status, pwd_lenght, abc, ABC, num, sym, removal_list
    char_types = ["abc", "ABC", "num", "sym"]
    available = ""
    pwd = ""

    for type in range(len(char_types)):
        if char_status[type] == 1:
            available += globals()[char_types[type]]

    for char in removal_list:
        available = available.replace(char, "")

    if available == "":
        output = f"{RED}EMPTY RESULT{RESET}"
        return output

    for char in range(pwd_lenght):
        pwd += random.choice(available)
    
    return pwd

# REMOVE DUPLICATE CHARS FROM REMOVAL LIST
def removal_duplicate():
    global removal_list
    removal_list = "".join(dict.fromkeys(removal_list))

# PROCESS USER PROMPT
def user_input():
    global output, pwd_lenght, char_status, removal_list
    single_status = [1, 2, 3, 4]
    possible_lenght = [8, 30]
    user_input = input()

    # GENERATE PASSWORD
    if user_input == "":
        output = generate_password()
        return output

    # QUITTING
    if user_input.lower() == "q":
        quit()

    # PASSWORD SAVING
    if user_input == "s":
        if output.startswith("\033"):
            output = f"{RED}SAVING ERROR{RESET}"
            return output
        else:
            with open("PyPassForge.key", "a") as file:
                file.write(f"{output}\n")
            output = f"{GREEN}PWD SAVED{RESET}"
            return output

    # PRINT REMOVAL LIST
    if user_input == "r":
        if removal_list == "":
            output = f"{RED}EMPTY LIST{RESET}"
            return output
        else:
            output = f"{BLUE}{removal_list}{RESET}"
            return output

    # RESET REMOVAL LIST
    if user_input == "R":
        removal_list = ""
        output = f"{GREEN}REMOVAL LIST CLEANED{RESET}"
        return output

    # CHECK FOR REMOVAL
    if user_input[0] == "r":
        user_input = user_input[1:]
        removal_list += user_input
        removal_duplicate()
        output = f"{GREEN}CHARS REMOVED{RESET}"
        return output
    
    # ADMIT CHAR BACK FROM REMOVAL LIST
    if user_input[0] == "a":
        user_input = user_input[1:]
        for char in user_input:
            removal_list = removal_list.replace(char, "")
        output = f"{GREEN}CHARS ADDED{RESET}"
        return output

    # BINARY CHAR TYPE SWITCH
    if len(user_input) == 4 and all(char in '01' for char in user_input):
        char_status = []
        for char in user_input:
            char_status.append(int(char))
        output = f"{GREEN}SETTINGS CHANGED{RESET}"
        return output

    # CONVERT NUMERIC INPUT INTO INTER
    if user_input.isdigit():
        user_input = int(user_input)
    
    # SINGLE CHAR TYPE SWITCH
    if user_input in single_status:
        if char_status[user_input - 1] == 1:
            char_status[user_input - 1] = 0
        else:
            char_status[user_input - 1] = 1
        output = f"{GREEN}SETTING CHANGED{RESET}"
        return output

    # PASSWORD LENGHT UPDATE
    if user_input in range(possible_lenght[0], possible_lenght[1] + 1):
        pwd_lenght = user_input
        output = f"{GREEN}PWD LENGTH CHANGED{RESET}"
        return output

    # NON RECOGNIZED PROMPT
    else:
        output = f"{RED}UNKNOWN PROMPT{RESET}"
        return output

def PyPassForge():
    while True:
        clear_terminal()
        print_ui("title")
        print_parameters()
        print_ui("instructions")
        print_output(output)
        user_input()

if __name__ == "__main__":
    PyPassForge()