# This is a game where you should guess a number 

import random

# generer et nummer 
number = random.randint(1,20)
print("I am thinking of a number between 1 and 20.\n you have 6 guesses to guess my number")

for guessTaken in range(1,6):
   guess = int(input())

# kontrollere hvert gæt om det er højere eller lavere end number
   if guess > number:
        print("Your guess is too high.")
   elif guess < number:
        print("your guess is too low")
   else:
        break

# Hvis det rigtige nummer er fundet inden for 6 forsøg printer den good job, da number = guess 
# ellers siger den hvad det rigtige nummer er 

if guess == number:
    print("good job you guessed my number in " + str(guessTaken)+ " gueses!")
else:
    print("Sorry mate, my number was: " + str(number) + " .")


