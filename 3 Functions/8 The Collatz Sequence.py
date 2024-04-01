


# Intro
print("This is the Collatz sequence. Every number you give me will eventually give the number 1 ")

# Try og except giver brugeren en ide til, hvorfor at programmet ikke virker
try:
    userInput = input("Please enter a a number: ")      
except ValueError:
    print("Please enter a valid interger")

# Dette while loop er grunden til at funtionen bliver kaldt indtil man rammer 1
while userInput != 1:
    userInput = collatz(int(userInput))

def collatz(number):
  
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            result = 3 * number + 1
            print(result)
            return result






