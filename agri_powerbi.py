# Power BI Python data preparation script
# Source: ICRISAT District Level Data CSV
#
# Power BI will import the final DataFrame named: df

import pandas as pd

# -------------------------------------------------------------------
# 1. Source file
# -------------------------------------------------------------------
# Change this path only if your CSV is stored somewhere else.
CSV_PATH = r"C:\Users\preet\ICRISAT-District Level Data - ICRISAT-District Level Data.csv"

# -------------------------------------------------------------------
# 2. Load data
# -------------------------------------------------------------------
df = pd.read_csv(CSV_PATH)

# -------------------------------------------------------------------
# 3. Basic cleaning
# -------------------------------------------------------------------

# Remove accidental spaces from column names.
df.columns = df.columns.str.strip()

# Remove completely empty rows and columns.
df = df.dropna(axis=0, how="all")
df = df.dropna(axis=1, how="all")

# Remove duplicate records.
df = df.drop_duplicates().reset_index(drop=True)

# Clean text columns without changing their column names.
text_columns = df.select_dtypes(include=["object"]).columns

for col in text_columns:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Convert Year to numeric when the column exists.
if "Year" in df.columns:
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Convert columns that are clearly numeric.
# This keeps text/state/district columns untouched.
for col in df.columns:
    if col != "Year" and (
        "PRODUCTION" in col
        or "AREA" in col
        or "YIELD" in col
    ):
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------------------------------------------------
# 4. Final DataFrame for Power BI
# -------------------------------------------------------------------
# IMPORTANT: Do not use print(), display(), plt.show(), get_ipython(),
# MySQL connections, or pip install commands here.
#
# Power BI uses the DataFrame named "df".
df
