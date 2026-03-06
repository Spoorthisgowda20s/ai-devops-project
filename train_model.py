import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset
data = {
    "Marketing_Spend": [1000, 2000, 3000, 4000, 5000],
    "Customer_Visits": [100, 150, 200, 250, 300],
    "Product_Price": [10, 10, 12, 12, 15],
    "Sales": [2000, 4000, 6000, 8000, 10000]
}

df = pd.DataFrame(data)

X = df[["Marketing_Spend", "Customer_Visits", "Product_Price"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("sales_model.pkl", "wb"))

print("Model trained and saved!")