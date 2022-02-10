from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('base.html')

@app.route("/homepage/", methods = ["POST", "GET"])
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        try:
            return render_template('homepage.html', name=request.form['name'], guru=request.form['guru'])
        except:
            return render_template('homepage.html')



@app.route("/recommender/<name>/", methods = ["POST", "GET"])
def chooseType(name):
    if request.method == "GET":
        return render_template("chooseType.html")

    else:
        try:
            return render_template("recommender.html", type=request.form['type'])
        except:
            return render_template("recommender.html")



@app.route("/recommender/<name>/", methods = ["POST", "GET"])
def recommender(name):
    if request.method == "GET":
        return render_template("recommender.html")

    else:
        return render_template("recommender.html")
