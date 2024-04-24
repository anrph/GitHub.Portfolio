import random
import string
import os

def clear():
    os.system('cls')

def print_status():
    if abc_status == "on":
        print(f"abc: {GREEN}on{RESET}   ", end = "")
    else:
        print(f"abc: {RED}off{RESET}  ", end = "")

    if ABC_status == "on":
        print(f"ABC: {GREEN}on{RESET}   ", end = "")
    else:
        print(f"ABC: {RED}off{RESET}  ", end = "")

    if num_status == "on":
        print(f"123: {GREEN}on{RESET}   ", end = "")
    else:
        print(f"123: {RED}off{RESET}  ", end = "")

    if sym_status == "on":
        print(f"#$&: {GREEN}on{RESET}   ")
    else:
        print(f"#$&: {RED}off{RESET}  ")

def generate_password():
    available = ""
    pwd = ""
    if abc_status == "on":
        available += abc
    if ABC_status == "on":
        available += ABC
    if num_status == "on":
        available += num
    if sym_status == "on":
        available += sym

    for i in range(pwd_lenght):
        pwd += random.choice(available)
    
    return pwd

CYAN = '\033[96m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

abc = string.ascii_lowercase
ABC = string.ascii_uppercase
num = string.digits
sym = string.punctuation

abc_status = "on"
ABC_status = "on"
num_status = "on"
sym_status = "on"

pwd_lenght = 10
result = ""

while True:
    clear()
    print(f"{CYAN}•--------------------------------------•\n PyPassForge 2.0.0 - By Alejandro Romeo\n•--------------------------------------•{RESET}")
    print_status()
    print("\nPress ENTER to generate a password")

    if all(status == "off" for status in (abc_status, ABC_status, num_status, sym_status)):
        result = f"{RED}EMPTY RESULT{RESET}"
    else:
        result = generate_password()

    print(f"{YELLOW}[{RESET}",result,f"{YELLOW}]{RESET}", end = " ")
    user_input = input()

    if user_input.isdigit():
        input_number = int(user_input)
    else:
        pass

    if user_input == "":
        continue

    if input_number >= 8 and input_number <= 30:
        pwd_lenght = input_number

    if input_number == 1:
        if abc_status == "on":
            abc_status = "off"
        else:
            abc_status = "on"
    
    if input_number == 2:
        if ABC_status == "on":
            ABC_status = "off"
        else:
            ABC_status = "on"
        
    if input_number == 3:
        if num_status == "on":
            num_status = "off"
        else:
            num_status = "on"
    
    if input_number == 4:
        if sym_status == "on":
            sym_status = "off"
        else:
            sym_status = "on"