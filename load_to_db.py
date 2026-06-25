import pandas as pd
import sqlite3
import os

os.makedirs("data/db", exist_ok=True)
DB_PATH = "data/db/bluestock_mf.db"

print("=" * 80)
print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 80)


conn = sqlite3.connect(DB_PATH)

with open("sql/schema.sql", "r") as f:
    schema_script = f.read()
conn.executescript(schema_script)
print("\n✅ Schema created (all tables).")


fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_sql("dim_fund", conn, if_exists="replace", index=False)
print(f"✅ dim_fund loaded: {fund_master.shape[0]} rows")


nav = pd.read_csv("data/processed/clean_nav.csv")
# Compute daily_return_pct
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav['daily_return_pct'] = nav.groupby('amfi_code')['nav'].pct_change() * 100
nav_to_load = nav.rename(columns={'date': 'nav_date'})[['amfi_code', 'nav_date', 'nav', 'daily_return_pct']]
nav_to_load.to_sql("fact_nav", conn, if_exists="replace", index=False)
print(f"✅ fact_nav loaded: {nav_to_load.shape[0]} rows")


txn = pd.read_csv("data/processed/clean_transactions.csv")
txn.to_sql("fact_transactions", conn, if_exists="replace", index=False)
print(f"✅ fact_transactions loaded: {txn.shape[0]} rows")


perf = pd.read_csv("data/processed/clean_performance.csv")
perf_cols = ['amfi_code', 'return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct',
             'benchmark_3yr_pct', 'alpha', 'beta', 'sharpe_ratio', 'sortino_ratio',
             'std_dev_ann_pct', 'max_drawdown_pct', 'aum_crore', 'morningstar_rating']
perf_to_load = perf[[c for c in perf_cols if c in perf.columns]]
perf_to_load.to_sql("fact_performance", conn, if_exists="replace", index=False)
print(f"✅ fact_performance loaded: {perf_to_load.shape[0]} rows")


aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_sql("fact_aum", conn, if_exists="replace", index=False)
print(f"✅ fact_aum loaded: {aum.shape[0]} rows")


sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
sip.to_sql("fact_sip_industry", conn, if_exists="replace", index=False)
print(f"✅ fact_sip_industry loaded: {sip.shape[0]} rows")


portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")
portfolio.to_sql("fact_portfolio", conn, if_exists="replace", index=False)
print(f"✅ fact_portfolio loaded: {portfolio.shape[0]} rows")

conn.commit()
conn.close()

print("\n" + "=" * 80)
print(f"DATABASE CREATED: {DB_PATH}")
print("ALL TABLES LOADED SUCCESSFULLY")
print("=" * 80)