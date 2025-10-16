from pathlib import Path

def main():
    """
    Locate the data files for the Week 2 activies
    and print whether they exist
    """

    # find the project root (tow levels up from this file)
    project_root = Path(__file__).resolve().parents[2]

    # build the file paths
    csv_file = project_root / "data" / "paralympics_raw.csv"
    excel_file = project_root
