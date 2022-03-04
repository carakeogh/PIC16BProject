from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import numpy as np
import functions

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
            return render_template("chooseType.html", type1=request.form['type1'])
        except:
            return render_template("chooseType.html")



@app.route("/<type1>/", methods = ["POST", "GET"])
def recommender(type1):
    df = functions.getData(type1)
    images = functions.randomSelect(df, 10)

    if request.method == "GET":
        return render_template("recommender.html", images = images)

    else:
        return render_template("recommender.html", images = images)


# @app.route("/similar_products/", method = ["POST", "GET"])
#def similar_products(style):

 #   if request.method == "GET":
  #      return render_template("similar_products.html")

   # else:
    #    return render_template("similar_products.html")