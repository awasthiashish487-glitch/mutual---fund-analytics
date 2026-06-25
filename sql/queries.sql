-- ============================================================
-- BLUESTOCK MF ANALYTICS - 10 ANALYTICAL QUERIES
-- ============================================================

-- 1. Top 5 funds by AUM
SELECT amfi_code, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month (for one sample fund, e.g. HDFC Top 100 = 125497)
SELECT strftime('%Y-%m', nav_date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
WHERE amfi_code = '125497'
GROUP BY month
ORDER BY month;

-- 3. SIP inflow YoY growth (latest 12 months)
SELECT month, sip_inflow_crore, yoy_growth_pct
FROM fact_sip_industry
ORDER BY month DESC
LIMIT 12;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense_ratio < 1%
SELECT amfi_code, scheme_name, fund_house, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct;

-- 6. Top 5 funds by Sharpe Ratio
SELECT amfi_code, sharpe_ratio, return_3yr_pct
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Number of schemes per fund house
SELECT fund_house, COUNT(*) AS num_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY num_schemes DESC;

-- 8. Transaction type breakdown (SIP vs Lumpsum vs Redemption)
SELECT transaction_type, COUNT(*) AS total_count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Average SIP amount by age group
SELECT age_group, AVG(amount_inr) AS avg_amount
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY age_group
ORDER BY avg_amount DESC;

-- 10. Funds with negative alpha (underperforming benchmark)
SELECT amfi_code, alpha, beta, return_3yr_pct, benchmark_3yr_pct
FROM fact_performance
WHERE alpha < 0
ORDER BY alpha ASC