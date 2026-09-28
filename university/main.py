from functions import show_separator, show_grades, get_status_by_avg
from settings import USER_INFO_FILE_PATH, USER_GRADES_FILE_PATH
import storage

import os


name = None
last_name = None
code = None

score_sum = 0
score_count = 0

max_score = None
min_score = None

avg = 0

grades = []

if os.path.isfile(USER_INFO_FILE_PATH):
    with open(USER_INFO_FILE_PATH) as file:
        name = file.readline().replace("\n", "")
        last_name = file.readline().replace("\n", "")
        code = file.readline().replace("\n", "")

if os.path.isfile(USER_GRADES_FILE_PATH):
    with open(USER_GRADES_FILE_PATH) as file:
        for grade in file.readlines():
            grade = grade.replace("\n", "")
            grades.append(grade)


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
        show_separator("Student Info")

        name = input("Name:")
        last_name = input("Last Name:")
        code = input("Student Number:")

        with open(USER_INFO_FILE_PATH, "w") as file:
            file.writelines(f"{name}\n{last_name}\n{code}")

        print("Student's information saved.")

        show_separator(char_sep_count=40)
        os.system("cls")
    # Insert Grades
    elif command == "2":
        show_separator()

        print("Type Exit in order to quit. Numbers should be between 0 to 20")
        while True:
            grade = input(f"Number {score_count + 1}:")
            if grade.lower() == "exit":
                break

            grade = float(grade)
            grades.append(grade)
            storage.garade_save(grade)

            score_sum += grade

            if max_score is None or grade > max_score:
                max_score = grade
            if min_score is None or grade < min_score:
                min_score = grade

            score_count += 1

        show_separator()
        os.system("cls")

    # Show Student Report
    elif command == "3":
        show_separator()

        # Calculating Average Score
        avg = score_sum / (len(grades))

        status, quote = get_status_by_avg(avg)

        print()
        print(f"Full Name: {name} {last_name}")
        print(f"Student ID: {code}")
        print(f"Average: {avg}")
        print(f"Status: {status}")
        print(f"Highest Score: {max_score}")
        print(f"Lowest Score: {min_score}")
        print(quote)
        show_separator()

    elif command == "4":
        show_separator()

        show_grades(grades)

        show_separator()
    elif command == "5":
        show_separator()

        show_grades(grades)

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

        show_grades(grades)

        show_separator()

    # Exit
    elif command == "0":
        break
    else:
        print("Wrong command.")

    print()
