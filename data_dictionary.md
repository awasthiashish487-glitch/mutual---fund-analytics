# Data Dictionary — Bluestock MF Analytics

| Column | Type | Description |
|--------|------|--------------|
| amfi_code | TEXT (PK) | Unique AMFI scheme code |
| scheme_name | TEXT | Full official scheme name |
| fund_house | TEXT | AMC name (e.g. SBI Mutual Fund) |
| category | TEXT | Equity / Debt |
| sub_category | TEXT | Large Cap / Mid Cap / Liquid etc. |
| plan | TEXT | Regular or Direct |
| launch_date | DATE | Fund launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| fund_manager | TEXT | Fund manager name |
| risk_category | TEXT | SEBI risk category |
| sebi_category_code | TEXT | Internal SEBI code |

| Column | Type | Description |
|--------|------|--------------|
| nav_id | INTEGER (PK) | Auto-increment ID |
| amfi_code | TEXT (FK) | Links to dim_fund |
| nav_date | DATE | NAV date |
| nav | REAL | NAV value in Rs. |
| daily_return_pct | REAL | Day-over-day % return |

| Column | Type | Description |
|--------|------|--------------|
| tx_id | INTEGER (PK) | Auto-increment ID |
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Date of transaction |
| amfi_code | TEXT (FK) | Fund involved |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Amount in INR |
| state, city, city_tier | TEXT | Investor location |
| age_group, gender | TEXT | Demographics |
| annual_income_lakh | REAL | Annual income (lakh) |
| payment_mode | TEXT | UPI / Net Banking / etc. |
| kyc_status | TEXT | Verified / Pending |

| Column | Type | Description |
|--------|------|--------------|
| amfi_code | TEXT (PK/FK) | Links to dim_fund |
| return_1yr_pct / 3yr / 5yr | REAL | Returns over period |
| benchmark_3yr_pct | REAL | Benchmark 3yr return |
| alpha, beta | REAL | Risk-adjusted metrics |
| sharpe_ratio, sortino_ratio | REAL | Risk-adjusted return ratios |
| std_dev_ann_pct | REAL | Annualised std deviation |
| max_drawdown_pct | REAL | Worst peak-to-trough decline |
| aum_crore | REAL | AUM in Rs. crore |
| morningstar_rating | INTEGER | 1-5 star rating |

| Column | Type | Description |
|--------|------|--------------|
| fund_house | TEXT | AMC name |
| quarter_date | DATE | Quarter end date |
| aum_crore | REAL | AUM in Rs. crore |
| num_schemes | INTEGER | Number of schemes |

| Column | Type | Description |
|--------|------|--------------|
| month | TEXT (PK) | YYYY-MM format |
| sip_inflow_crore | REAL | Monthly SIP inflow |
| active_sip_accounts_crore | REAL | Active SIP accounts |
| new_sip_accounts_lakh | REAL | New registrations |
| sip_aum_lakh_crore | REAL | Total SIP AUM |
| yoy_growth_pct | REAL | YoY growth % |

| Column | Type | Description |
|--------|------|--------------|
| amfi_code | TEXT (FK) | Fund |
| stock_symbol | TEXT | Stock held |
| weight_pct | REAL | Weight in portfolio (%) |
| sector | TEXT | Sector classification |
| holding_date | DATE | As-of date |
