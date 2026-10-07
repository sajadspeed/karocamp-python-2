import json
import os


courses = []

if os.path.isfile("./courses.json"):
    with open("./courses.json") as file:
        courses = json.loads(file.read())

while True:
    print(courses)

    name = input("Name: ")
    grade = input("Grade: ")
    unit = input("Unit: ")

    course = {"name": name, "grade": grade, "unit": unit}

    courses.append(course)

    courses_json = json.dumps(courses, indent=4)

    with open("./courses.json", "w") as file:
        file.write(courses_json)
