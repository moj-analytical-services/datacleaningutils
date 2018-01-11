# -*- coding: utf-8 -*-

"""
Data cleaning functions that clean up date columns
"""

import datetime

import logging
import pandas as pd

log = logging.getLogger(__name__)

def convert_pd_columns_to_date(df, cols, format_precidence="%Y-%m-%d", errors='raise'):
    """Convert columns in a pandas dataframe into dates (i.e. datetime.date, not datetimes)

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
        df = _convert_pd_column_to_date(df, c, format_precidence, errors)

    return df

def _convert_pd_column_to_date(df, col, format_precidence, errors):
    successfully_converted = False
    for f in format_precidence:
        try:
            df[col] = pd.to_datetime(df[col], errors=errors, format=f)
            successfully_converted = True
            break
        except ValueError:
            pass

    if not successfully_converted:
        # Find first value that couldn't be converted by any of the formats in format precident
        for r in df.iterrows():
            index = r[0]
            row = r[1]
            cell = row[col]
            found_format = False
            for f in format_precidence:
                try:
                    datetime.datetime.strptime(cell, f)
                    found_format = True
                except (ValueError, TypeError):
                    pass
            if not found_format:
                message = "Problem at index {}: Value in column {} = {} isn't in formats {}"
                message = message.format(index, col, cell, format_precidence)
                raise ValueError(message)

        raise ValueError()
    else:
        df[col] = df[col].dt.date

    return df

def find_and_log_pd_date_parse_errors(col, format="%Y-%m-%d"):
    """Convert columns in a pandas dataframe into dates (i.e. datetime.date, not datetimes)

    Args:
        col: A pandas series
        format: Strftime format to try https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html

    Returns:
        df: The dataframe with the relevant columns converted to dates
    """

    errors_set = set()
    new_col = []
    for cell in col:
        try:
            parsed = datetime.datetime.strptime(cell, format)
            new_col.append(parsed.date())
        except:
            errors_set = errors_set.union([cell])
            new_col.append("error in {}".format(cell))

    for date in errors_set:
        log.info("Failed to parse '{}' with format {}".format(date, format))
