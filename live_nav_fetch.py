import requests
import pandas as pd
import os

# Output folder
RAW_DATA_PATH = "data/raw"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

# Scheme code -> Scheme name mapping
schemes = {
    "125497": "HDFC_Top100",
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_LargeCap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

print("=" * 80)
print("LIVE NAV FETCH REPORT")
print("=" * 80)

for code, name in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract NAV history
        nav_data = data.get("data", [])
        df = pd.DataFrame(nav_data)

        # Save as CSV
        file_path = os.path.join(RAW_DATA_PATH, f"live_nav_{name}.csv")
        df.to_csv(file_path, index=False)

        print(f"\n✅ {name} (Code: {code})")
        print(f"   Scheme Name: {data.get('meta', {}).get('scheme_name', 'N/A')}")
        print(f"   Rows fetched: {df.shape[0]}")
        print(f"   Saved to: {file_path}")

    except Exception as e:
        print(f"\n❌ Error fetching {name} (Code: {code}): {e}")

print("\n" + "=" * 80)
print("LIVE NAV FETCH COMPLETE")
print("=" * 80)