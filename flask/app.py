from flask import Flask, render_template

app = Flask("MySite")


@app.route("/hello")
def hello_world():
    return "سلام دنیای عزیزم."


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/profile")
def profile_page():
    user = {
        "name": "Ilia",
        "age": 22,
        "phone": "09135268745",
        "national_code": "16513215",
        "address": "Esf, Be to che.",
    }
    return render_template("profile.html", user=user)


@app.route("/users")
def users_page():
    users = [
        {
            "name": "Ilia",
            "age": 22,
            "phone": "09135268745",
            "national_code": "16513215",
            "address": "Esf, Be to che.",
        },
        {
            "name": "Hassan",
            "age": 22,
            "phone": "09135268745",
            "national_code": "16513215",
            "address": "Esf, Be to che.",
        },
        {
            "name": "Mohamad",
            "age": 22,
            "phone": "09135268745",
            "national_code": "16513215",
            "address": "Esf, Be to che.",
        },
        {
            "name": "Aria",
            "age": 22,
            "phone": "09135268745",
            "national_code": "16513215",
            "address": "Esf, Be to che.",
        },
    ]
    return render_template("users.html", users=users)


app.run(port=80, debug=True)
