'''
# Helper Functions

## Objective

The objective of this module is to create reusable helper functions that can be used across multiple dashboard pages.

Instead of writing common operations repeatedly, we centralize them in a single file.

This improves:

- Code reusability
- Maintainability
- Readability
- Consistency

These helper functions will support formatting, validation, and small utility operations used throughout the dashboard.
'''

"""
Helper Functions
----------------

This module contains reusable helper functions used
throughout the Streamlit dashboard.

Author: Arin Bhardwaj
Project: Intelligent Customer Analytics Platform
"""

from typing import Union
import pandas as pd


# ============================================================
# Currency Formatting
# ============================================================

def format_currency(value: Union[int, float]) -> str:
    """
    Convert a numeric value into a formatted currency string.

    Example:
        12543.5 -> ₹12,543.50
    """

    return f"₹{value:,.2f}"


# ============================================================
# Percentage Formatting
# ============================================================

def format_percentage(value: Union[int, float]) -> str:
    """
    Convert decimal value into percentage.

    Example:
        0.823 -> 82.30%
    """

    return f"{value * 100:.2f}%"


# ============================================================
# Large Number Formatting
# ============================================================

def format_number(value: Union[int, float]) -> str:
    """
    Format large numbers for better readability.

    Example:

    1500      -> 1.5K
    2500000   -> 2.5M
    """

    if abs(value) >= 1_000_000:
        return f"{value/1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"{value/1_000:.2f}K"

    return f"{value:.0f}"


# ============================================================
# Check Empty DataFrame
# ============================================================

def is_dataframe_empty(df: pd.DataFrame) -> bool:
    """
    Check whether a dataframe is empty.
    """

    return df.empty


# ============================================================
# Safe Division
# ============================================================

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers.

    Returns 0 if denominator is zero.
    """

    if denominator == 0:
        return 0

    return numerator / denominator


# ============================================================
# Customer Type
# ============================================================

def customer_type(customer_id, customer_list):
    """
    Determine whether a customer is new or existing.
    """

    if customer_id in customer_list:
        return "Existing Customer"

    return "New Customer"