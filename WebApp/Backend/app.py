from flask import Flask, request, jsonify
import pickle
import pandas as pd


app = Flask(__name__)

# initiate model & columns

with open("grid_KNR_final.pkl", "rb") as f:
    model = pickle.load(f)

columns = ['brand','model','year','title_status','mileage','color','country']


@app.route("/")
def welcome():
    return "<h3>Selamat Datang di Program Backend Model Saya</h3>"

@app.route("/predict", methods=["GET", "POST"])
def predict_price():
    if request.method == "POST":
        content = request.json
        try:
            data= {'brand': content['brand'],
                   'model':content['model'],
                   'year':content['year'],
                   'title_status':content['title_status'],
                   'mileage':content['mileage'],
                   'color': content['color'],
                   'country': content['country']}
            data = pd.DataFrame([data])
            res = model.predict(data).tolist()
             

            response = jsonify(success=True, result=res)
            return response, 200
        except Exception as e:
            response = jsonify(success=False,
                               message=str(e))
            return response, 400
    # return dari method get
    return "<p>Silahkan gunakan method POST untuk mode <em>inference model</em></p>"

# app.run()


