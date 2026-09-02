name = None
last_name = None
code = None

score_sum = 0
score_count = 0

max_score = None
min_score = None

avg = 0


while True:
    print("--- UN Management ---")
    print("1. Insert Student Information")
    print("2. Insert Grades")
    print("3. Show Student Report")

    print("0. Exit")

    print()

    command = input("Enter your command: ")

    # Insert Student Info
    if command == "1":
        name = input("Name:")
        last_name = input("Last Name:")
        code = input("Student Number:")

        print("Student's information saved.")

    # Insert Grades
    elif command == "2":
        print("Type Exit in order to quit. Numbers should be between 0 to 20")
        while True:
            score = input(f"Number {score_count + 1}:")
            if score.lower() == "exit":
                break

            score = float(score)

            score_sum += score

            if max_score is None or score > max_score:
                max_score = score
            if min_score is None or score < min_score:
                min_score = score

            score_count += 1

    # Show Student Report
    elif command == "3":
        pass

    # Exit
    elif command == "0":
        break
    else:
        print("Wrong command.")

    print()
