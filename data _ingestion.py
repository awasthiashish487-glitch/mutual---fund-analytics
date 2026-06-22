import requests
import pandas as pd
import os

# Folder banao
os.makedirs("data/raw", exist_ok=True)

# 5 schemes jo task mein diye hain
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
    print(f"✅ Saved: {filename} — {len(df)} rows")