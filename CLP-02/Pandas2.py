import pandas as pd

# Use raw string (r"") or double backslashes to avoid invalid escape sequences
df = pd.read_csv(r"C:\clp\sales_data.csv")

# Ensure numeric_only=True for compatibility with newer Pandas versions
df_filled = df.fillna(df.mean(numeric_only=True))

print(df_filled)
