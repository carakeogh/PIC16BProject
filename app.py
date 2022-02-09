from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("homepage.html")


@app.route("/", methods = ["POST", "GET"])
def start():
    if request.method == "GET":
        return render_template("start.html")

    else:
        try:
            return render_template("start.html", name = request.form['name'])
        except:
            return render_template("recommender.html")


@app.route("/", methods = ["POST", "GET"])
def recommender():
    if request.method == "GET":
        return render_template("recommender.html")

    else:
        return render_template("recommender.html")