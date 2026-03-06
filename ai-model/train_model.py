from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

hours = np.array([[1],[2],[3],[4],[5]])
marks = np.array([35,40,50,60,70])

model = LinearRegression()
model.fit(hours, marks)

joblib.dump(model, "model.pkl")

print("Model trained!")