import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")


our_codes = [125497, 119551, 120503, 118632, 119092, 120841]

print("=== AMFI CODE VALIDATION ===\n")

for code in our_codes:
    exists = code in fund_master['schemeCode'].values
    status = "✅ EXISTS" if exists else "❌ NOT FOUND"
    print(f"Code {code}: {status}")

print(f"\nTotal funds in master: {len(fund_master)}")
print(f"Our codes checked: {len(our_codes)}")

print("\n=== DATA QUALITY SUMMARY ===")
print(f"Null values:\n{fund_master.isnull().sum()}")