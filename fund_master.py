import pandas as pd

# Load fund master CSV
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 80)
print("FUND MASTER EXPLORATION REPORT")
print("=" * 80)

print(f"\nTotal schemes: {df.shape[0]}")
print(f"Total columns: {df.shape[1]}")
print(f"\nColumns: {list(df.columns)}")

# Unique fund houses
print("\n" + "-" * 80)
print(f"Unique Fund Houses ({df['fund_house'].nunique()}):")
print(df['fund_house'].unique())

# Unique categories
print("\n" + "-" * 80)
print(f"Unique Categories ({df['category'].nunique()}):")
print(df['category'].unique())

# Unique sub-categories
print("\n" + "-" * 80)
print(f"Unique Sub-Categories ({df['sub_category'].nunique()}):")
print(df['sub_category'].unique())

# Unique risk grades
print("\n" + "-" * 80)
print(f"Unique Risk Categories ({df['risk_category'].nunique()}):")
print(df['risk_category'].unique())

# AMFI scheme code structure
print("\n" + "-" * 80)
print("Sample AMFI Codes & SEBI Category Codes:")
print(df[['amfi_code', 'scheme_name', 'sebi_category_code']].head(10))

print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION COMPLETE")
print("=" * 80)