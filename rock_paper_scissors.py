import random

list = ["Rock", "Paper", "Scissors"]

user = input("Enter your choice (Rock/Paper/Scissors):\t").title()
Bot = random.choice(list)       #Generate a random choice for the bot


print(f"You chose: {user}")
print(f"Bot chose: {Bot}")

if user not in list:
    print("Invalid choice!")    #Handles unexpected Entries

#Draw Condition    
elif user == Bot:
    print("It's a draw!")

#winning conditions for the user
elif (user == "Rock" and Bot == "Scissors") or \
     (user == "Paper" and Bot == "Rock") or \
     (user == "Scissors" and Bot == "Paper"):
    print("You win!")

#Lossing vondition
else:
    print("Bot🤖 wins! ")