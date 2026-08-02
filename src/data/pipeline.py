"""
Data Pipeline Module

Combines loading, validation and cleaning into one pipeline.
"""

from config.config import RAW_DATA_PATH

from src.data.loader import DataLoader
from src.data.validator import DataValidator
from src.data.cleaner import DataCleaner


class DataPipeline:
    """
    Complete Data Cleaning Pipeline
    """

    def __init__(self):

        self.loader = DataLoader(RAW_DATA_PATH)
        self.validator = DataValidator()
        self.cleaner = DataCleaner()

    def run(self):

        # Step 1 : Load Dataset
        df = self.loader.load_data()

        # Step 2 : Validate Dataset
        self.validator.validate(df)

        # Step 3 : Clean Dataset
        clean_df = self.cleaner.clean(df)

        # Step 4 : Save Dataset
        self.cleaner.save_cleaned_data(clean_df)

        # Step 5 : Cleaning Summary
        self.cleaner.show_summary()

        return clean_df