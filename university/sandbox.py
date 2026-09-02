name = input("Name:")
last_name = input("Last Name:")
code = input("Student Number:")

score_sum = 0
score_count = 0

max_score = None
min_score = None

avg = 0

# Getting Scores
print("Type Exit in order to quit. Numbers should be between 0 to 20")
while True:
    score = input(f"Number {score_count}:")
    if score.lower() == "exit":
        break

    score = float(score)

    score_sum += score

    if max_score is None or score > max_score:
        max_score = score
    if min_score is None or score < min_score:
        min_score = score

    score_count += 1

avg = score_sum / (score_count)

# Comprehending The Score
if avg == 20:
    Status = "an excellent"
    quote = " Sadly you're a low-life nerd."
elif 20 > avg >= 17:
    Status = "a pretty good"
    quote = " tbh? meh, you will never be good enough."
elif 17 > avg >= 14:
    Status = "a decent"
    quote = " You are mid."
elif 14 > avg >= 10:
    Status = "a mediocre"
    quote = " You are not good at this. think about a job."
elif 10 > avg >= 5:
    Status = "a terrible"
    quote = " You are a failure. A failure to me and to your parents."
elif 5 > avg > 1:
    Status = "a miserable"
    quote = " Consider suicide."
elif 1 > avg > 0:
    Status = "a atrocious"
    quote = "\nWHY? WHY DONT'T YOU KILL YOURSELF? JUST END IT!"
elif avg == 0:
    Status = "No"
    quote = "\nYou dropped your crown, King."
else:
    Status = "No valid"
    quote = "\nWhat are you doing lil bro? enter a proper score."
    avg = "Not valid"

print(
    f"{name} {last_name} with the student number of {code}, Your average score is {avg}"
)
print(f"You have {Status} rating.", end=quote)
