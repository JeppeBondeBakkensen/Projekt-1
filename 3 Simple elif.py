print("Please enter your name: ")
userInput = input() # User enter there name

print("Please enter your age")
age = int(input()) # User enter there age
if userInput == "Jeppe":
    print("Hello" + userInput)
elif age < 12:
    print(userInput + " you are to young to be Jeppe")
elif age > 2000:
    print("Hello vampire from another life")
elif age > 100:
    print(userInput + " you are not Jeppe, Granni")
else: 
    print("You are neither Jeppe or a kid")