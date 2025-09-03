import os
import joblib

def test_model_exists():
    assert os.path.exists("model.pkl")

def test_model_predict():
    model = joblib.load("model.pkl")
    y_pred = model.predict([[1.0]])
    assert isinstance(y_pred[0], float)
