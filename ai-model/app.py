from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    hours = np.array([[data["hours"]]])
    prediction = model.predict(hours)[0]
    return jsonify({"predicted_marks": float(prediction)})

app.run(host="0.0.0.0", port=5000)