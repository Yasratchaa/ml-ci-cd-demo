import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load dataset dari file CSV
df = pd.read_csv("data/housing.csv")

X = df.drop("MedHouseValue", axis=1)
y = df["MedHouseValue"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"✅ Model trained. RMSE: {rmse:.2f}")

# Simpan model
joblib.dump(model, "model.pkl")
print("✅ Model disimpan ke model.pkl")
