import numpy as np
import pandas as pd
import datetime
def rough_heuristic_column_type_check(column, metadata_type, num_checks=10):
    """
    This function is a very quick heuristic/rule of thumb that
    should check the data type of a column

    It will spot errors a good proportion of the time, but you will likely experience false positives and false negatives

    It will raise a ValueError if it finds a problem

    Args:
        columns: A pandas seris
        metadata_type:  The metadata type, see https://github.com/moj-analytical-services/data_engineering_utils/blob/master/dataengineeringutils/data/data_type_conversion.csv
        num_checks: How many data points in the column to sample for the checks.
    Returns:
        None

    """
    # The type of NaN is float so any column with a None in will be float, even if all other numbers are ints
    type_checks = {
        "character" : {type(None), str},
        "int": {np.int64, np.float64},
        "float": {np.float64},
        "date": {datetime.date, type(None), pd._libs.tslib.NaTType}
    }

    value_checks = {
        "character" : {},
        "int": {pd.np.nan},
        "float": {pd.np.nan},
        "date": {pd.NaT, pd.np.nan}
    }

    sample_size = min(num_checks, len(column))
    this_column = column.sample(sample_size)

    possible_types = type_checks[metadata_type]
    possible_values = value_checks[metadata_type]

    for val in this_column:
        if type(val) not in possible_types and val not in possible_values:
            message = "The value {} in column {} is of type {} which is not in possible types {}"
            message = message.format(val, column.name, type(val), possible_types)
            raise ValueError(message)

