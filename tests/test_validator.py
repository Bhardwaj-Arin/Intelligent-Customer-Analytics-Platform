import pandas as pd

from src.data.validator import validate_data


def test_validate_data():

    df = pd.DataFrame({

        "CustomerID":[1],

        "InvoiceNo":["1001"],

        "Revenue":[200]

    })

    assert validate_data(df) == True