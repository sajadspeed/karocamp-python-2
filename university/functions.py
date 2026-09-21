def show_separator(title="", char_sep="=", char_sep_count=40):
    print()
    if title == "":
        print(char_sep * char_sep_count)
    else:
        char_sep_count -= len(title)
        if is_even(char_sep_count):
            char_sep_count -= 1
        else:
            char_sep_count -= 1
        print(
            char_sep * int(char_sep_count / 2),
            title,
            char_sep * int(char_sep_count / 2),
        )
    print()


def is_even(number):
    return number % 2 == 0


def show_grades(grades):
    if len(grades) > 0:
        i = 0
        while i < len(grades):
            print(i + 1, f" => ** {grades[i]} **")

            i += 1
    else:
        print("No grades available.")


def get_status_by_avg(avg):
    """
    return {status: "", quote: ""}
    """
    status = ""
    quote = ""
    if avg == 20:
        status = "Excellent"
        quote = "Sadly you're a low-life nerd."
    elif 20 > avg >= 17:
        status = "Good"
        quote = "tbh? meh, you will never be good enough."
    elif 17 > avg >= 14:
        status = "Decent"
        quote = "You are mid."
    elif 14 > avg >= 10:
        status = "Mediocre"
        quote = "You are not good at this. think about a job."
    elif 10 > avg >= 5:
        status = "Terrible"
        quote = "You are a failure. A failure to me and to your parents."
    elif 5 > avg >= 1:
        status = "Miserable"
        quote = "Consider suicide."
    elif 1 > avg > 0:
        status = "Atrocious"
        quote = "WHY? WHY DONT'T YOU KILL YOURSELF? JUST END IT!"
    elif avg == 0:
        status = "No"
        quote = "You dropped your crown, King."
    else:
        status = "Not valid"
        quote = "What are you doing lil bro? enter a proper score."

    return {"status": status, "quote": quote}
