"""
Data Loading Module

Loads the raw dataset.
"""

from pathlib import Path

import pandas as pd


class DataLoader:

    def __init__(self, data_path):

        self.data_path = Path(data_path)

    def load_data(self):

        print("=" * 60)

        print("LOADING DATASET")

        print("=" * 60)

        df = pd.read_csv(

            self.data_path,

            encoding="ISO-8859-1"

        )

        print(f"Rows Loaded    : {df.shape[0]:,}")

        print(f"Columns Loaded : {df.shape[1]}")

        print("=" * 60)

        return df