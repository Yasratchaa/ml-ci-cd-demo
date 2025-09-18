import os
import joblib

def test_model_exists():
    assert os.path.exists("model.pkl")

def test_model_predict():
    model = joblib.load("model.pkl")
    y_pred = model.predict([[8.3252, 41, 6.9841, 1.0238, 322, 2.5556, 37.88, -122.23]])
    assert y_pred.shape[0] == 1
