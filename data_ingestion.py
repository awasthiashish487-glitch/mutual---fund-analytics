import pandas as pd
import os

RAW_DATA_PATH = "data/raw"

csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

dataframes = {}

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

for file_name in csv_files:
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    try:
        df = pd.read_csv(file_path)
        dataframes[file_name] = df

        print(f"\n📄 File: {file_name}")
        print("-" * 80)
        print(f"Shape: {df.shape}")
        print(f"\nData types:\n{df.dtypes}")
        print(f"\nFirst 5 rows:\n{df.head()}")

        missing = df.isnull().sum()
        if missing.sum() > 0:
            print(f"\n⚠️ Missing values:\n{missing[missing > 0]}")
        else:
            print("\n✅ No missing values.")
    except Exception as e:
        print(f"\n❌ Error loading {file_name}: {e}")

print("\n" + "=" * 80)
print("DATA INGESTION COMPLETE")
print("=" * 80)