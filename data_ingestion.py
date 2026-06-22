import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

# Step 1: API se CSV fetch karo
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['data'])
    df['scheme_name'] = data['meta']['scheme_name']
    filename = f"data/raw/{name}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved: {filename}")

# Step 2: Har CSV load karke info print karo
print("\n--- CSV FILES INFO ---\n")
for name in schemes.keys():
    filename = f"data/raw/{name}.csv"
    df = pd.read_csv(filename)
    print(f"File: {name}")
    print(f"Shape: {df.shape}")
    print(f"Dtypes:\n{df.dtypes}")
    print(f"Head:\n{df.head()}")
    print("-" * 50)