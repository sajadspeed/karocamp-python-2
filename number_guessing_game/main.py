import random

difficulties = {
    "easy": {"max_number": 100, "max_guess": 10},
    "normal": {"max_number": 300, "max_guess": 7},
    "hard": {"max_number": 700, "max_guess": 5},
    "iran": {"max_number": 10000, "max_guess": 3},
}

i = 1
for difficulty in difficulties:
    print(
        f"{i}. {difficulty.title()} 1-{difficulties[difficulty]['max_number']} Guess: {difficulties[difficulty]['max_guess']}"
    )

    i += 1

game_dificulty = None

choose = int(input("Enter your sdlkfjs: "))
if choose == 1:
    game_dificulty = difficulties["easy"]
elif choose == 2:
    game_dificulty = difficulties["normal"]
elif choose == 3:
    game_dificulty = difficulties["hard"]
else:
    game_dificulty = difficulties["iran"]


computer_number = random.randint(1, game_dificulty["max_number"])
guess_count = 0
guess_max = game_dificulty["max_guess"]

while True:
    user_number = int(
        input(
            f"({guess_count}/{guess_max})Enter your guess(1, {game_dificulty['max_number']}): "
        )
    )
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
