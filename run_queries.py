import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

# Read all queries from file, split by semicolon
with open("sql/queries.sql", "r") as f:
    content = f.read()

queries = [q.strip() for q in content.split(";") if q.strip() and not q.strip().startswith("--")]

print("=" * 80)
print("RUNNING 10 ANALYTICAL QUERIES")
print("=" * 80)

for i, query in enumerate(queries, 1):
    # Remove comment lines within query
    clean_query = "\n".join([line for line in query.split("\n") if not line.strip().startswith("--")]).strip()
    if not clean_query:
        continue
    try:
        print(f"\n{'-'*80}")
        print(f"QUERY {i}:")
        print(clean_query[:100] + "..." if len(clean_query) > 100 else clean_query)
        print("-" * 80)
        result = pd.read_sql_query(clean_query, conn)
        print(result)
    except Exception as e:
        print(f"❌ Error in query {i}: {e}")

conn.close()
print("\n" + "=" * 80)
print("ALL QUERIES EXECUTED")
print("=" * 80)