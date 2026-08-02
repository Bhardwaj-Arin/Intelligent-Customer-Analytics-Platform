"""
Data Cleaning Module

Performs all cleaning operations on the raw dataset.
"""

from pathlib import Path
import pandas as pd

from config.config import (
    DATE_COLUMN,
    PRICE_COLUMN,
    QUANTITY_COLUMN,
)

from config.paths import PROCESSED_DATA_DIR


class DataCleaner:
    """
    Cleans the Online Retail II dataset.
    """

    def __init__(self):

        self.cleaning_summary = {}

    # ==========================================================
    # Main Function
    # ==========================================================

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        print("\n")
        print("=" * 60)
        print("STARTING DATA CLEANING")
        print("=" * 60)

        original_rows = len(df)

        df = self.remove_duplicates(df)

        df = self.convert_datetime(df)

        df = self.remove_missing_description(df)

        df = self.remove_missing_customer(df)

        df = self.remove_invalid_price(df)

        df = self.create_cancellation_column(df)

        df = self.create_total_amount(df)

        df = df.reset_index(drop=True)

        self.cleaning_summary["Original Rows"] = original_rows
        self.cleaning_summary["Final Rows"] = len(df)
        self.cleaning_summary["Rows Removed"] = original_rows - len(df)

        print("\nCleaning Completed Successfully.")
        print("=" * 60)

        return df

    # ==========================================================
    # Duplicate Removal
    # ==========================================================

    def remove_duplicates(self, df):

        duplicates = df.duplicated().sum()

        print(f"\nDuplicate Rows Found : {duplicates:,}")

        df = df.drop_duplicates()

        print("Duplicate Rows Removed")

        return df

    # ==========================================================
    # Datetime Conversion
    # ==========================================================

    def convert_datetime(self, df):

        df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])

        print("\nInvoiceDate converted to datetime.")

        return df

    # ==========================================================
    # Missing Description
    # ==========================================================

    def remove_missing_description(self, df):

        before = len(df)

        df = df.dropna(subset=["Description"])

        removed = before - len(df)

        print(f"\nRemoved Missing Description : {removed:,}")

        return df

    # ==========================================================
    # Missing Customer ID
    # ==========================================================

    def remove_missing_customer(self, df):

        before = len(df)

        df = df.dropna(subset=["Customer ID"])

        removed = before - len(df)

        print(f"Removed Missing Customer ID : {removed:,}")

        return df

    # ==========================================================
    # Invalid Price
    # ==========================================================

    def remove_invalid_price(self, df):

        before = len(df)

        df = df[df[PRICE_COLUMN] > 0]

        removed = before - len(df)

        print(f"Removed Invalid Price Rows : {removed:,}")

        return df

    # ==========================================================
    # Cancellation Flag
    # ==========================================================

    def create_cancellation_column(self, df):

        df["IsCancelled"] = df["Invoice"].astype(str).str.startswith("C")

        cancelled = df["IsCancelled"].sum()

        print(f"\nCancelled Transactions : {cancelled:,}")

        return df

    # ==========================================================
    # Total Amount
    # ==========================================================

    def create_total_amount(self, df):

        df["TotalAmount"] = df[QUANTITY_COLUMN] * df[PRICE_COLUMN]

        print("Created TotalAmount Column.")

        return df

    # ==========================================================
    # Save Dataset
    # ==========================================================

    def save_cleaned_data(self, df):

        PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

        output_path = PROCESSED_DATA_DIR / "cleaned_online_retail.csv"

        df.to_csv(output_path, index=False)

        print("\nCleaned dataset saved successfully.")

        print(output_path)

    # ==========================================================
    # Cleaning Summary
    # ==========================================================

    def show_summary(self):

        print("\n")
        print("=" * 60)
        print("CLEANING SUMMARY")
        print("=" * 60)

        for key, value in self.cleaning_summary.items():

            print(f"{key:<20}: {value:,}")

        print("=" * 60)