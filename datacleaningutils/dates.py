# -*- coding: utf-8 -*-

"""
Data cleaning functions that clean up date columns
"""

from datetime import datetime
import logging
import pandas as pd

log = logging.getLogger(__name__)

def convert_pd_columns_to_date(df, cols, format_precidence=["%Y-%m-%d"], errors='raise'):
    """Add two numbers together using pandas Series.sum()

    Args:
        df: A pandas dataframe
        cols: The names of the columns to convert
        errors: Whether to ignore errors using the errors parameter of pd.to_datetime
        format_precidence: List of strftimes to try https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html

    Returns:
        df: The dataframe with the relevant columns converted to dates
    """

    # If user has provided a single format
    if type(format_precidence) == str:
        format_precidence = [format_precidence]

    # If user has provided a single column
    if type(cols) == str:
        cols = [cols]

    for c in cols:
        df[c] = _convert_pd_column_to_date(df[c], format_precidence, errors)
        for f in format_precidence:
            try:
                df[c] = pd.to_datetime(df[c], errors = errors, format=f)
            except ValueError:
                for r in df.iterrows():
                    index = r[0]
                    row = r[1]
                    cell = row[c]
                    try:
                        date = datetime.strptime(cell, this_format)
                    except ValueError:
                        message = "Problem in row {} at index {}, value {} isn't in format {}".format(row, index, cell, this_format)
                        raise ValueError(message)
            df[c] = df[c].dt.date
    return df

def _convert_pd_column_to_date(col, format_precidence, errors):
    for f in format_precidence:
            try:
                df[c] = pd.to_datetime(df[c], errors = errors, format=f)
            except ValueError:
                for r in df.iterrows():
                    index = r[0]
                    row = r[1]
                    cell = row[c]
                    try:
                        date = datetime.strptime(cell, this_format)
                    except ValueError:
                        message = "Problem in row {} at index {}, value {} isn't in format {}".format(row, index, cell, this_format)
                        raise ValueError(message)
            df[c] = df[c].dt.date



df = pd.read_csv("tests/data/dates.csv")
df

col_to_convert = "date_2"
this_format = "%Y-%m-%d"
df2 = convert_pd_columns_to_date(df, col_to_convert, ["%Y-%m-%d"])

df2