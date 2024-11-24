greeting = input("Greetings:")
new_greeting = greeting.lower().strip()

if "hello" in new_greeting:
    print("$0")

elif "h" == new_greeting[0]:
    print("$20")

else:
    print("$100")
