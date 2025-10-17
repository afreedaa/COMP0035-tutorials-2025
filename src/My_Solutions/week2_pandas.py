from pathlib import Path

import pandas as pd

def main():
    """
    Locate the data files for the Week 2 activies
    and print whether they exist
    """

    # find the project root (two levels up from this file)
    project_root = Path(__file__).resolve().parents[1]

    # build the file paths
    csv_file = project_root / "activities" / "data" / "paralympics_raw.csv"
    excel_file = project_root / "activities" / "data" / "paralympics_all_raw.xlsx"

    # check if the files exist
    print(f"CSV path: {csv_file}")
    print(f"Excel path: {excel_file}")
    print("CSV exsits?", csv_file.exists())
    print("Excel exists?", excel_file.exists())

    """
    Load the CSV and Excel datasets into pandas DataFrames
    """
    print(f"Loading CSV from {csv_file}")
    print(f"Loading Excel from {excel_file}")

    events_csv_df = pd.read_csv(csv_file)
    events_excel_df = pd.read_excel(excel_file, sheet_name=0)
    medals_excel_df = pd.read_excel(excel_file, sheet_name=1)

    """
    Print basic information, shape, columns, and stats for a DataFrame.
    """
    print(f"\n=== {name} Info ===")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nData Types:")
    print(df.dtypes)
    print("\nTail:")
    print(df.tail())
    print("\nInfo:")
    print(df.info())
    print("\nDescribe:")
    print(df.describe())


