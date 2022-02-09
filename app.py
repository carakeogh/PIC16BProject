from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("homepage.html")

@app.route("/start/", methods = ["POST", "GET"])
def start():
    if request.method == "GET":
        return render_template("start.html")
    else:
        try:
            return render_template("start.html", guru=request.form["guru"])
        except:
            return render_template("start.html")
