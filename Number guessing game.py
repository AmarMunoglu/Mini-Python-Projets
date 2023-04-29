import random
from random import *

print("Welcome to the guessing game!")
print("You are asked to guess a random nnumber between 0 and 10. You have 5 chances. If you guess correct, you win, and if noy, you lose!")

the_number = randint(0,10)

def guess():
    life = 5
    check = True
    while check:
        if life > 0:
            user_input = int(input("Guess -> : "))
        
            if user_input == the_number:
                print(f'You won, the number was {the_number}')
                check = False
                break
            elif user_input > the_number:
                print('Lower!')
                life -= 1
                continue
            elif user_input < the_number:
                print('Higher!')
                life -= 1
                continue
        else:
            print('You lost. You had 5 chances! The number was {the_number}.')
            check = False

print(guess())