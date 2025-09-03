from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import joblib

# generate data dummy
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)
model = LinearRegression().fit(X, y)

# simpan model
joblib.dump(model, "model.pkl")
print("Model trained and saved as model.pkl")
