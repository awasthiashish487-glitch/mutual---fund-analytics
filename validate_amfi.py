import pandas as pd

# Load both datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 80)
print("AMFI CODE VALIDATION REPORT")
print("=" * 80)

# Get unique codes from both
fund_master_codes = set(fund_master['amfi_code'].unique())
nav_history_codes = set(nav_history['amfi_code'].unique())

print(f"\nTotal unique AMFI codes in fund_master: {len(fund_master_codes)}")
print(f"Total unique AMFI codes in nav_history: {len(nav_history_codes)}")

# Codes in fund_master but missing from nav_history
missing_in_nav = fund_master_codes - nav_history_codes

# Codes in nav_history but not in fund_master (extra/unexpected)
extra_in_nav = nav_history_codes - fund_master_codes

print("\n" + "-" * 80)
print("DATA QUALITY SUMMARY")
print("-" * 80)

if len(missing_in_nav) == 0:
    print("✅ All AMFI codes in fund_master exist in nav_history.")
else:
    print(f"⚠️ {len(missing_in_nav)} AMFI code(s) in fund_master are MISSING from nav_history:")
    print(missing_in_nav)

if len(extra_in_nav) == 0:
    print("✅ No extra/unexpected AMFI codes found in nav_history.")
else:
    print(f"⚠️ {len(extra_in_nav)} AMFI code(s) in nav_history are NOT in fund_master:")
    print(extra_in_nav)

# Row counts per scheme in nav_history
print("\n" + "-" * 80)
print("NAV row count per scheme (first 10):")
print(nav_history['amfi_code'].value_counts().head(10))

print("\n" + "=" * 80)
print("VALIDATION COMPLETE")
print("=" * 80)