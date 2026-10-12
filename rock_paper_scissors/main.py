import random

CHOICES = ["Rock", "Paper", "Scissors"]

while True:
    print("1. Rock 🤘")
    print("2. Paper 📃")
    print("3. Scissors ✂")

    user_choice = CHOICES[int(input("Enter your choice: ")) - 1]

    computer_choice = random.choice(CHOICES)

    if user_choice == computer_choice:
        print("Draw...")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You won.")
    else:
        print(
            "You lost something in your life and you can't back to normal life again because your a such peac......"
        )
