from __init__ import app, db
from flask import Flask, render_template, request, redirect, url_for
from preprocessing import predict
from model import Facts, PersonalityTypes
import pandas as pd
import random 

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        # input_df = None
        # if request.form:
        #     input_df = pd.DataFrame(request.form.to_dict(flat=False))
        #     input_df.drop(columns = ['submit'], inplace = True)
        # if not input_df.empty:
        #     ans = predict(input_df)
        #     type_ = PersonalityTypes.query.filter_by(ptype = ans).first()
        pass
    else:
        facts = Facts.query.all()
        t = random.choices(facts, k = 3)
        print(t)
        return render_template('index.html', facts = t)

@app.route('/result', methods = ["POST", "GET"])
def results():
    if request.method == "POST":
        input_df = None
        if request.form:
            input_df = pd.DataFrame(request.form.to_dict(flat=False))
            input_df.drop(columns = ['submit'], inplace = True)
        if not input_df.empty:
            ans = predict(input_df)
            type_ = PersonalityTypes.query.filter_by(ptype = ans).first()
        return render_template('result.html', type = type_)

if __name__ == "__main__":
    app.run(debug = True)
