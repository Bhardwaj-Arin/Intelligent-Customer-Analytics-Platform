"""
Data Cleaning Module

Performs all cleaning operations on the raw dataset and produces
the single canonical transaction-level dataset used by every
notebook and every dashboard page in this project:

    data/processed/final_cleaned_dataset.csv

Canonical schema produced by this module:

    InvoiceNo, StockCode, Description, Quantity, InvoiceDate,
    UnitPrice, CustomerID, Country, IsCancelled, Revenue,
    Year, Month, MonthName, Day, DayName, Hour, Quarter,
    DayOfWeek, Week, IsWeekend, TimeOfDay

Previously, this module only produced an intermediate dataset
(cleaned_online_retail.csv) using the raw column names (Invoice,
Price, "Customer ID", TotalAmount). A separate, one-off cell in
the Phase 3 EDA notebook then renamed those columns and derived
Revenue and the time-based features, saving the result as
final_cleaned_dataset.csv. That meant the canonical dataset only
existed if someone had manually run that notebook cell by hand,
and the transformation logic lived nowhere in version-controlled,
reusable code. This module now owns that transformation directly,
so `DataPipeline().run()` alone is enough to reproduce the
canonical dataset from raw data every time.
"""

from pathlib import Path
import pandas as pd

from config.config import (
    DATE_COLUMN,
    PRICE_COLUMN,
    QUANTITY_COLUMN,
)

from config.paths import FINAL_CLEANED_DATA_PATH


# ================================================================
# Canonical Schema
# ================================================================

# Raw -> canonical column renames. Applied after the raw-schema
# cleaning steps (which still refer to the raw names below), and
# before Revenue and the time-based features are derived.
CANONICAL_COLUMN_RENAMES = {
    "Invoice": "InvoiceNo",
    "Price": "UnitPrice",
    "Customer ID": "CustomerID",
}

# Final column order for the canonical dataset.
CANONICAL_COLUMN_ORDER = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
    "IsCancelled",
    "Revenue",
    "Year",
    "Month",
    "MonthName",
    "Day",
    "DayName",
    "Hour",
    "Quarter",
    "DayOfWeek",
    "Week",
    "IsWeekend",
    "TimeOfDay",
]


class DataCleaner:
    """
    Cleans the Online Retail II dataset and produces the
    canonical transaction-level dataset used throughout the
    project.
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

        # ---- Raw-schema cleaning steps ----
        # These operate on the raw column names (Invoice, Price,
        # "Customer ID") exactly as they appear in the source
        # dataset, before any renaming happens.

        df = self.remove_duplicates(df)

        df = self.convert_datetime(df)

        df = self.remove_missing_description(df)

        df = self.remove_missing_customer(df)

        df = self.remove_invalid_price(df)

        df = self.create_cancellation_column(df)

        # ---- Canonical schema steps ----
        # From here on, the dataset is transformed into the
        # single canonical schema used by every later phase and
        # the dashboard.

        df = self.rename_to_canonical_columns(df)

        df = self.create_revenue_column(df)

        df = self.create_time_features(df)

        df = self.enforce_canonical_schema(df)

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
    # Rename to Canonical Column Names
    # ==========================================================

    def rename_to_canonical_columns(self, df):

        df = df.rename(columns=CANONICAL_COLUMN_RENAMES)

        print(
            "\nRenamed columns to canonical schema: "
            f"{CANONICAL_COLUMN_RENAMES}"
        )

        return df

    # ==========================================================
    # Revenue
    # ==========================================================

    def create_revenue_column(self, df):

        df["Revenue"] = df[QUANTITY_COLUMN] * df["UnitPrice"]

        print("Created Revenue column.")

        return df

    # ==========================================================
    # Time-Based Features
    # ==========================================================

    def create_time_features(self, df):
        """
        Derive every time-based feature used across the project
        (Year, Month, MonthName, Day, DayName, Hour, Quarter,
        DayOfWeek, Week, IsWeekend, TimeOfDay) from InvoiceDate.
        """

        df["Year"] = df["InvoiceDate"].dt.year

        df["Month"] = df["InvoiceDate"].dt.month

        df["MonthName"] = df["InvoiceDate"].dt.month_name()

        df["Day"] = df["InvoiceDate"].dt.day

        df["DayName"] = df["InvoiceDate"].dt.day_name()

        df["Hour"] = df["InvoiceDate"].dt.hour

        df["Quarter"] = df["InvoiceDate"].dt.quarter

        df["DayOfWeek"] = df["InvoiceDate"].dt.dayofweek

        df["Week"] = df["InvoiceDate"].dt.isocalendar().week.astype(int)

        df["IsWeekend"] = df["DayOfWeek"].isin([5, 6])

        df["TimeOfDay"] = df["Hour"].apply(self._bucket_time_of_day)

        print("Created time-based features (Year, Month, MonthName, "
              "Day, DayName, Hour, Quarter, DayOfWeek, Week, "
              "IsWeekend, TimeOfDay).")

        return df

    @staticmethod
    def _bucket_time_of_day(hour):
        """
        Bucket an hour (0-23) into a named part of the day.

        06:00-11:59 -> Morning
        12:00-16:59 -> Afternoon
        17:00-20:59 -> Evening
        21:00-05:59 -> Night
        """

        if 6 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 17:
            return "Afternoon"
        elif 17 <= hour < 21:
            return "Evening"
        else:
            return "Night"

    # ==========================================================
    # Enforce Canonical Schema
    # ==========================================================

    def enforce_canonical_schema(self, df):
        """
        Select and order columns to exactly match
        CANONICAL_COLUMN_ORDER, so the saved dataset always has
        a predictable, consistent schema regardless of any
        incidental column ordering earlier in the pipeline.
        """

        missing = [
            column
            for column in CANONICAL_COLUMN_ORDER
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Cannot produce the canonical dataset - missing "
                f"expected columns: {missing}"
            )

        return df[CANONICAL_COLUMN_ORDER]

        # ==========================================================
    # Save Dataset
    # ==========================================================

    def save_cleaned_data(self, df):

        FINAL_CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        # Float columns
        float_cols = [
            "UnitPrice",
            "Revenue"
        ]

        for col in float_cols:
            df[col] = df[col].astype("float32")

        # Integer columns
        int_cols = [
            "Quantity",
            "Year",
            "Month",
            "Day",
            "Hour",
            "Quarter",
            "DayOfWeek",
            "Week"
        ]

        for col in int_cols:
            df[col] = pd.to_numeric(df[col], downcast="integer")

        # Boolean
        df["IsWeekend"] = df["IsWeekend"].astype("bool")
        df["IsCancelled"] = df["IsCancelled"].astype("bool")

        # Category columns
        category_cols = [
            "Country",
            "MonthName",
            "DayName",
            "TimeOfDay"
        ]

        for col in category_cols:
            df[col] = df[col].astype("category")

        df.to_csv(
            FINAL_CLEANED_DATA_PATH,
            index=False,
            float_format="%.2f"
        )

        print("\nCanonical dataset saved successfully.")
        print(FINAL_CLEANED_DATA_PATH)

        size_mb = FINAL_CLEANED_DATA_PATH.stat().st_size / (1024 * 1024)

        print(f"\nDataset Size : {size_mb:.2f} MB")

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