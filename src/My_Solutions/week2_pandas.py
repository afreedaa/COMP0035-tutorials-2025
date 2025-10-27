# week2_pandas_describe.py
import pandas as pd
from pathlib import Path


def get_data_path() -> Path:
    """Return the path to the CSV file."""
    base_dir = Path(__file__).parent.parent / "activities" / "data"
    return base_dir / "paralympics_raw.csv"


def load_data(csv_path: Path) -> pd.DataFrame:
    """Read the CSV into a DataFrame."""
    return pd.read_csv(csv_path)


def describe_dataframe(df: pd.DataFrame, name: str = "DataFrame") -> None:
    """
    Print a structured summary of a pandas DataFrame.

    Args:
        df: The DataFrame to describe.
        name: A label for display in the console output.
    """
    print(f"\n--- {name} DESCRIPTION ---")
    print(f"Shape (rows, columns): {df.shape}")
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
    print("\nNon-null info:")
    df.info()  # prints directly
    print("\nSummary statistics:")
    print(df.describe(include="all", datetime_is_numeric=True))
    print("\nFirst five rows:")
    print(df.head())
    print("\nLast five rows:")
    print(df.tail())
    print("\n--------------------------")


def main() -> None:
    """Main function to load and describe the dataset."""
    csv_path = get_data_path()
    df = load_data(csv_path)
    describe_dataframe(df, name="Paralympics Events")


if __name__ == "__main__":
    main()






