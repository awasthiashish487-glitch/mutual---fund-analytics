import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

print("=" * 80)
print("CLEANING: nav_history.csv")
print("=" * 80)


df = pd.read_csv("data/raw/02_nav_history.csv")
print(f"\nOriginal shape: {df.shape}")


df['date'] = pd.to_datetime(df['date'])


df = df.sort_values(by=['amfi_code', 'date']).reset_index(drop=True)

before = df.shape[0]
df = df.drop_duplicates(subset=['amfi_code', 'date'])
after = df.shape[0]
print(f"Duplicates removed: {before - after}")

cleaned_groups = []
for code, group in df.groupby('amfi_code'):
    group = group.set_index('date')
    full_range = pd.date_range(start=group.index.min(), end=group.index.max(), freq='D')
    group = group.reindex(full_range)
    group['amfi_code'] = code
    group['nav'] = group['nav'].ffill()
    cleaned_groups.append(group)

df_clean = pd.concat(cleaned_groups).reset_index().rename(columns={'index': 'date'})


invalid_nav = df_clean[df_clean['nav'] <= 0]
print(f"Invalid NAV (<=0) rows found: {invalid_nav.shape[0]}")
df_clean = df_clean[df_clean['nav'] > 0]

print(f"\nFinal cleaned shape: {df_clean.shape}")
print(f"\nMissing values after cleaning:\n{df_clean.isnull().sum()}")

output_path = "data/processed/clean_nav.csv"
df_clean.to_csv(output_path, index=False)
print(f"\n✅ Saved cleaned file to: {output_path}")

print("\n" + "=" * 80)
print("NAV HISTORY CLEANING COMPLETE")
print("=" * 80)
print("\n" + "=" * 80)
print("CLEANING: investor_transactions.csv")
print("=" * 80)

txn = pd.read_csv("data/raw/08_investor_transactions.csv")
print(f"\nOriginal shape: {txn.shape}")
print(f"Columns: {list(txn.columns)}")

# 1. Standardise transaction_type
txn['transaction_type'] = txn['transaction_type'].str.strip().str.title()
print(f"\nUnique transaction types: {txn['transaction_type'].unique()}")

# 2. Validate amount > 0
invalid_amount = txn[txn['amount_inr'] <= 0]
print(f"Invalid amount (<=0) rows: {invalid_amount.shape[0]}")
txn = txn[txn['amount_inr'] > 0]

# 3. Check KYC status values
print(f"\nKYC status values: {txn['kyc_status'].unique()}")

# 4. Fix date formats
txn['transaction_date'] = pd.to_datetime(txn['transaction_date'], errors='coerce')
invalid_dates = txn[txn['transaction_date'].isnull()]
print(f"Invalid/unparsable dates: {invalid_dates.shape[0]}")
txn = txn.dropna(subset=['transaction_date'])

# Remove exact duplicates
before = txn.shape[0]
txn = txn.drop_duplicates()
after = txn.shape[0]
print(f"Duplicate rows removed: {before - after}")

print(f"\nFinal cleaned shape: {txn.shape}")
print(f"\nMissing values after cleaning:\n{txn.isnull().sum()}")

output_path = "data/processed/clean_transactions.csv"
txn.to_csv(output_path, index=False)
print(f"\n✅ Saved cleaned file to: {output_path}")

print("\n" + "=" * 80)
print("INVESTOR TRANSACTIONS CLEANING COMPLETE")
print("=" * 80)
print("\n" + "=" * 80)
print("CLEANING: scheme_performance.csv")
print("=" * 80)

perf = pd.read_csv("data/raw/07_scheme_performance.csv")
print(f"\nOriginal shape: {perf.shape}")
print(f"Columns: {list(perf.columns)}")

# 1. Validate return values are numeric
numeric_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct', 'sharpe_ratio',
                 'sortino_ratio', 'std_dev_ann_pct', 'max_drawdown_pct', 'alpha', 'beta']

for col in numeric_cols:
    if col in perf.columns:
        non_numeric = pd.to_numeric(perf[col], errors='coerce').isnull().sum()
        if non_numeric > 0:
            print(f"⚠️ {col}: {non_numeric} non-numeric value(s) found")
        perf[col] = pd.to_numeric(perf[col], errors='coerce')

# 2. Flag negative Sharpe ratios
negative_sharpe = perf[perf['sharpe_ratio'] < 0]
print(f"\nFunds with negative Sharpe ratio: {negative_sharpe.shape[0]}")
if negative_sharpe.shape[0] > 0:
    print(negative_sharpe[['amfi_code', 'sharpe_ratio']])

# 3. Check expense_ratio range (0.1% – 2.5%) -- from fund_master
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
out_of_range = fund_master[(fund_master['expense_ratio_pct'] < 0.1) | (fund_master['expense_ratio_pct'] > 2.5)]
print(f"\nFunds with expense_ratio outside 0.1%-2.5%: {out_of_range.shape[0]}")
if out_of_range.shape[0] > 0:
    print(out_of_range[['amfi_code', 'expense_ratio_pct']])

# Drop rows where critical numeric fields are still null after coercion
before = perf.shape[0]
perf = perf.dropna(subset=['sharpe_ratio', 'return_1yr_pct'])
after = perf.shape[0]
print(f"\nRows dropped due to invalid numeric data: {before - after}")

print(f"\nFinal cleaned shape: {perf.shape}")
print(f"\nMissing values after cleaning:\n{perf.isnull().sum()}")

output_path = "data/processed/clean_performance.csv"
perf.to_csv(output_path, index=False)
print(f"\n✅ Saved cleaned file to: {output_path}")

print("\n" + "=" * 80)
print("SCHEME PERFORMANCE CLEANING COMPLETE")
print("=" * 80)