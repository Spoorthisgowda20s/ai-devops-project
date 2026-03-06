from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("sales_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    marketing = float(request.form["marketing"])
    visits = float(request.form["visits"])
    price = float(request.form["price"])

    prediction = model.predict([[marketing, visits, price]])

    return render_template(
        "index.html",
        prediction_text=f"Predicted Sales: ${prediction[0]:,.2f}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)