import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)


url = "https://api.mfapi.in/mf"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
print("Total funds:", len(df))
print("\nColumns:", df.columns.tolist())
print("\nHead:\n", df.head())

df.to_csv("data/raw/fund_master.csv", index=False)
print("\nFund master saved!")

print("\n--- UNIQUE VALUES ---")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")
    print(df[col].unique()[:5])
    print()