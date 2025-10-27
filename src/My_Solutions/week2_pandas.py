from pathlib import Path

import pandas as pd

csv_file = Path(__file__).parent.parent.joinpath('activities','data', 'paralympics_raw.csv')

xlxs_file = Path(__file__).parent.parent.joinpath('activities','data', 'paralympics_all_raw.xlsx')

read_paralympics_csv = pd.read_csv(csv_file)






