from settings import USER_GRADES_FILE_PATH


def garade_save(grade):
    with open(USER_GRADES_FILE_PATH, "a") as file:
        file.write(str(grade) + "\n")
