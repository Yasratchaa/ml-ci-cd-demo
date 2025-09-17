from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_and_save_model():
    # Load California housing dataset
    data = fetch_california_housing()
    X, y = data.data, data.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Simpan model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model California Housing berhasil dilatih dan disimpan ke model.pkl")

if __name__ == "__main__":
    train_and_save_model()
