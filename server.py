from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "Gr3at_numb3r_key736"


@app.route("/")
def index():
    import random

    random.randint(1, 100)
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def grab_num():
    print("User Guess")
    print(request.form["user_num_input"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8009)
