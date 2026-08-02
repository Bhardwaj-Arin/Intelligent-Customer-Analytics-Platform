"""
Data Validation Module

Performs basic validation before cleaning.
"""

import pandas as pd

from config.config import REQUIRED_COLUMNS


class DataValidator:

    def validate(self, df: pd.DataFrame):

        print("\n")

        print("=" * 60)

        print("DATA VALIDATION REPORT")

        print("=" * 60)

        self.check_required_columns(df)

        self.check_missing_values(df)

        self.check_duplicates(df)

        self.check_negative_values(df)

        self.check_data_types(df)

        print("=" * 60)

        print("Validation Completed")

        print("=" * 60)

    def check_required_columns(self, df):

        missing = [

            column

            for column in REQUIRED_COLUMNS

            if column not in df.columns

        ]

        if len(missing) == 0:

            print("✓ Required Columns : PASSED")

        else:

            print("✗ Missing Columns")

            print(missing)

    def check_missing_values(self, df):

        print("\nMissing Values")

        missing = df.isnull().sum()

        missing = missing[missing > 0]

        if len(missing) == 0:

            print("No Missing Values")

        else:

            print(missing)

    def check_duplicates(self, df):

        duplicates = df.duplicated().sum()

        print(f"\nDuplicate Rows : {duplicates:,}")

    def check_negative_values(self, df):

        negative_quantity = (df["Quantity"] < 0).sum()

        negative_price = (df["Price"] < 0).sum()

        print(f"\nNegative Quantity : {negative_quantity:,}")

        print(f"Negative Price    : {negative_price:,}")

    def check_data_types(self, df):

        print("\nData Types")

        print(df.dtypes)