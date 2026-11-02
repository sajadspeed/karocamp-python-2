from flask import Flask, render_template, request, abort

import user_manager

app = Flask("MySite")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/hello")
def hello_world():
    return "سلام دنیای عزیزم."


@app.route("/")
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


@app.route("/search", methods=["POST", "GET"])
def search_page():
    username_for_search = request.args.get("username")

    user = user_manager.find_user(username_for_search)

    if user is None:
        return abort(404)

    users = [user]
    return render_template("search_users.html", users=users)


app.run(port=80, debug=True)
