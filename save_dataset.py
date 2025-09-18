import pandas as pd
from sklearn.datasets import fetch_california_housing

# Ambil dataset California Housing
housing = fetch_california_housing(as_frame=True)
df = pd.concat([housing.data, housing.target.rename("MedHouseValue")], axis=1)

# Simpan ke CSV
df.to_csv("data/housing.csv", index=False)
print("✅ Dataset disimpan ke data/housing.csv")
