import random

computer_number = random.randint(1, 1000)
guess_count = 0
guess_max = 3

while True:
    user_number = int(input("Enter your guess(1, 1000): "))
    guess_count += 1

    if user_number == computer_number:
        print("You won.")
        break
    elif user_number > computer_number:
        print("Lower...")
    elif user_number < computer_number:
        print("Higher...")

    if guess_count >= guess_max:
        print("You lose.")
        break

print(f"Computer number: {computer_number}")
