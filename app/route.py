from flask import render_template, request, redirect, url_for
from app import app
from app.Clean import clean
import joblib
import requests # <- ne pas installer 


model_load = joblib.load(filename='./app/review_allocine.pkl')


@app.route('/', methods=["GET", "POST"])   # == @app.route('/index')
def index():

    if request.method == "GET":
        # avis = request.form["review"]
        # result = (model_load[0].predict(model_load[1].transform(clean.nettoyage([avis]))))
        return render_template('index.html',reviews_form=3)

    if request.method == "POST":

            # avis = request.args.get("avis")
            avis = request.form["review"]
            result = (model_load[0].predict(model_load[1].transform(clean.nettoyage([avis]))))
            result = int(result)
            return render_template('index.html', reviews_form=result)

