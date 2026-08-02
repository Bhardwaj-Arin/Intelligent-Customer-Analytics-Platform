"""
Project Configuration

Stores project-wide constants.
"""

from config.paths import RAW_DATA_DIR

# ================================================================
# Dataset
# ================================================================

DATASET_NAME = "online_retail_II.csv"

RAW_DATA_PATH = RAW_DATA_DIR / DATASET_NAME

# ================================================================
# Required Columns
# ================================================================

REQUIRED_COLUMNS = [

    "Invoice",

    "StockCode",

    "Description",

    "Quantity",

    "InvoiceDate",

    "Price",

    "Customer ID",

    "Country"

]

# ================================================================
# Important Columns
# ================================================================

DATE_COLUMN = "InvoiceDate"

CUSTOMER_COLUMN = "Customer ID"

PRICE_COLUMN = "Price"

QUANTITY_COLUMN = "Quantity"

# ================================================================
# Random Seed
# ================================================================

RANDOM_STATE = 42