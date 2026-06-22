import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()

print("Scheme:", data['meta']['scheme_name'])
print("Latest NAV:", data['data'][0])

df = pd.DataFrame(data['data'])
df.to_csv("data/raw/live_nav_HDFC.csv", index=False)
print("Live NAV saved!")