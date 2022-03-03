from flask import Flask, render_template, request
#import random
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
import functions

app = Flask(__name__)

#def getData(type1):
   # df = pd.read_csv("styles.csv", nrows=10000, error_bad_lines=False)
   # image_df = pd.read_csv("images.csv")
   # df['filename'] = df.apply(lambda row: str(row['id']) + ".jpg", axis=1)

    # merge images.csv and styles.csv together
    #df = pd.merge(df, image_df, on = ["filename"])
   # df = df.sample(frac=1).reset_index(drop=True)

   # return df[df['subCategory'] == type1]

#def randomSelect(df, k):
  #  return random.sample(set(df["link"]), k)

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
    images = functions.randomSelect(df, 30)

    if request.method == "GET":
        return render_template("recommender.html", images = images)

    else:
        return render_template("recommender.html", images = images)
