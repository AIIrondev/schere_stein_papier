import time
import random
import sys
import pygame

index1 = None
computer_choice = ['Schere', 'Stein', 'Papier']
print('Lass uns Schere, Stein, Papier spielen!')

#Logic system
while True:
    random_1 = random.choice(computer_choice)
    user_input = input(">>>")
    if user_input == 'Exit':
        sys.exit(1)
    elif user_input == "help":
        print("Schere, Stein, Papier bitte eingeben um zu spielen!")
        print("Exit um das Spiel zu beenden!")
    elif random_1 == "Schere":
        if user_input == "Schere":
            print("Keiner hat gewonnen!")
        if user_input == "Papier":
            print("Du hast verlohren!")
        if user_input == "Stein":
            print("Du hast gewonnen!")
    elif random_1 == "Papier":
        if user_input == "Papier":
            print("Keiner hat gewonnen!")
        if user_input == "Stein":
            print("Du hast verlohren!")
        if user_input == "Schere":
            print("Du hast gewonnen!")
    elif random_1 == "Stein":
        if user_input == "Stein":
            print("Keiner hat gewonnen!")
        if user_input == "Schere":
            print("Du hast verlohren!")
        if user_input == "Papier":
            print("Du hast gewonnen!")
