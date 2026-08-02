import pandas as pd

from src.data.cleaner import clean_data


def test_clean_data():

    sample = pd.DataFrame({

        "CustomerID":[1,2,None],

        "Quantity":[10,-2,5],

        "UnitPrice":[5,10,-1]

    })

    cleaned = clean_data(sample)

    assert cleaned.isnull().sum().sum() == 0

    assert (cleaned["Quantity"] > 0).all()

    assert (cleaned["UnitPrice"] > 0).all()