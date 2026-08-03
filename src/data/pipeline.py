"""
Data Pipeline Module

Combines loading, validation and cleaning into one pipeline.

Running DataPipeline().run() is now the single, reproducible way
to produce data/processed/final_cleaned_dataset.csv - the one
canonical transaction dataset used by every later notebook
(Phase 4 onward) and every dashboard page.
"""

from config.config import RAW_DATA_PATH

from src.data.loader import DataLoader
from src.data.validator import DataValidator
from src.data.cleaner import DataCleaner


class DataPipeline:
    """
    Complete Data Cleaning Pipeline.

    Produces the canonical final_cleaned_dataset.csv from the
    raw Online Retail II dataset in one run.
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

        # Step 3 : Clean Dataset & Build Canonical Schema
        clean_df = self.cleaner.clean(df)

        # Step 4 : Save Canonical Dataset
        self.cleaner.save_cleaned_data(clean_df)

        # Step 5 : Cleaning Summary
        self.cleaner.show_summary()

        return clean_df