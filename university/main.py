from functions import show_separator


name = None
last_name = None
code = None

score_sum = 0
score_count = 0

max_score = None
min_score = None

avg = 0

grades = [20, 15, 18, 10]


while True:
    print("--- UN Management ---")
    print("1. Insert Student Information")
    print("2. Insert Grades")
    print("3. Show Student Report")
    print("4. Show grades")
    print("5. Remove grade")

    print("0. Exit")

    print()

    command = input("Enter your command: ")

    # Insert Student Info
    if command == "1":
        show_separator()

        name = input("Name:")
        last_name = input("Last Name:")
        code = input("Student Number:")

        print("Student's information saved.")

        show_separator()
    # Insert Grades
    elif command == "2":
        show_separator()

        print("Type Exit in order to quit. Numbers should be between 0 to 20")
        while True:
            score = input(f"Number {score_count + 1}:")
            if score.lower() == "exit":
                break

            score = float(score)
            grades.append(score)

            score_sum += score

            if max_score is None or score > max_score:
                max_score = score
            if min_score is None or score < min_score:
                min_score = score

            score_count += 1

        show_separator()

    # Show Student Report
    elif command == "3":
        show_separator()
        # Code in here
        show_separator()

    elif command == "4":
        show_separator()

        if len(grades) > 0:
            ### Show Grades
            i = 0
            while i < len(grades):
                print(i + 1, f" => ** {grades[i]} **")

                i += 1
            ###

        else:
            print("No grades available.")

        show_separator()
    elif command == "5":
        show_separator()

        ### Show Grades

        i = 0
        while i < len(grades):
            print(i + 1, f" => ** {grades[i]} **")

            i += 1
        ###

        grade = float(input("Enter grade for remove: "))

        ### Find grade in grades
        found_grade = False

        i = 0
        while i < len(grades):
            if grade == grades[i]:
                found_grade = True
            i += 1

        if found_grade:
            grades.remove(grade)
        else:
            print("Not found.")

        ### Show Grades
        i = 0
        while i < len(grades):
            print(i + 1, f" => ** {grades[i]} **")

            i += 1
        ###

        show_separator()

    # Exit
    elif command == "0":
        break
    else:
        print("Wrong command.")

    print()
