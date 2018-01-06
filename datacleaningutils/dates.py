# -*- coding: utf-8 -*-

"""
Data cleaning functions that clean up date columns
"""

import logging
import pandas as pd

log = logging.getLogger(__name__)

def convert_pd_columns_to_date(df, cols):
    """Add two numbers together using pandas Series.sum()

    Args:
        df: A pandas dataframe
        cols: The names of the columns to convert

    Returns:
        df: The dataframe with the relevant columns converted to dates
    """

    for c in cols:
        df[c] = pd.to_datetime(df[c], dayfirst = True ,errors = 'coerce')
    return df
