from flask import Flask, render_template

import user_manager

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
    users = user_manager.get_users()
    return render_template("users.html", users=users)


app.run(port=80, debug=True)
