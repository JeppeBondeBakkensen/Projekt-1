while True: 
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. what is your password? (Its a fish)")
    password = input()
    if password == "Swordfish":
        break 
print("Access granted")