from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import numpy as np
from py.functions import *
from py.algorithm import *

app = Flask(__name__)

# main page
@app.route("/")
def main():
    return render_template('base.html')

# homepage
@app.route("/homepage/", methods = ["POST", "GET"])
def homepage():
    if request.method == 'GET':
        return render_template('homepage.html')
    else:
        try:
            return render_template('homepage.html', name=request.form['name'], guru=request.form['guru'])
        except:
            return render_template('homepage.html')

# choose type of clothing page
@app.route("/recommender/<name>/", methods = ["POST", "GET"])
def chooseType(name):
    if request.method == "GET":
        return render_template("chooseType.html")

    else:
        try:
            return render_template("chooseType.html", type1=request.form['type1'])
        except:
            return render_template("chooseType.html")

# get users' style preferences
@app.route("/<type1>/", methods = ["POST", "GET"])
def recommender(type1):
    # prepare image data
    df = getData(type1)
    # randomly select 5 images to get users' preferences
    images = randomSelect(df, 5)

    if request.method == "GET":
        return render_template("recommender.html", images = images)

    else:
        try:
            return render_template("recommender.html", style = match(request.form['style']))
        except:
            return render_template("recommender.html", images = images)


# show recommended outfits
@app.route("/similarproducts/<style>/", methods = ["POST", "GET"])
def similar_products(style):

    if request.method == "GET":
        # prepare image data
        files = start()[1]
        # run our recommender model and get cosine similarity score on each data
        data = model(files)
        # get the five closest products
        imgs = recommended_outfit(data, start()[0] + style)
        # plot our result
        plots = plot(imgs)
        
        return render_template("similar_products.html", images = plots)
    
    else:
        try:
            return render_template("similar_products.html", repeat = request.form['repeat'])
        except:
            return render_template("similar_products.html")
