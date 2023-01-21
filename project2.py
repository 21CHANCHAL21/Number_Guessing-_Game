# Guess the number game

import random

number = random.randint(1, 10)
Guess = int(input("Enter the number:"))
print("Computer chosen", number)
print("You have chossen", Guess)

if Guess == number:
    print("Congretulations you guessed the number")

else:
    print("Bad! you are not able to guessed try again ")




