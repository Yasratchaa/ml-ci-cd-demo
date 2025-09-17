import os
import pickle
import numpy as np

def test_model_exists():
    assert os.path.exists("model.pkl")

def test_model_predict():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    y_pred = model.predict(np.random.rand(1, 8))  # 8 fitur California housing
    assert y_pred.shape == (1,)
