# -*- coding: utf-8 -*-

"""
Tests
"""
import datetime
import unittest
import pandas as pd
from datacleaningutils.data_types import rough_heuristic_pd_column_type_check

class DataTypeTest(unittest.TestCase):
    """
    Test the add function
    """

    def test_data_types_1(self):
        """
        Test first row of dates.csv is successfully converted
        """

        date = datetime.date(2017,1,1)
        date2 = datetime.date(2017,6,4)
        df = pd.DataFrame({"a": ["a", None, ""],
                            "b": [1,None,3],
                            "c":["2017-01-01", "2017-02-01", ""],
                            "d": [date, date2, None],
                            "e": [1.1,None,1.3]})

        df["c"] =  pd.to_datetime(df["c"]).dt.date

        rough_heuristic_pd_column_type_check(df["a"], "character")
        rough_heuristic_pd_column_type_check(df["b"], "int")
        rough_heuristic_pd_column_type_check(df["c"], "date")
        rough_heuristic_pd_column_type_check(df["d"], "date")
        rough_heuristic_pd_column_type_check(df["e"], "float")


if __name__ == '__main__':
    unittest.main()
