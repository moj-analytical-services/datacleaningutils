# -*- coding: utf-8 -*-

"""
Tests
"""
import datetime
import unittest
import pandas as pd
from datacleaningutils.dates import convert_pd_columns_to_date
from datacleaningutils.dates import find_and_log_pd_date_parse_errors

class DateTest(unittest.TestCase):
    """
    Test the add function
    """

    def test_convert_pd_columns_to_date_1(self):
        """
        Test first row of dates.csv is successfully converted
        """

        df = pd.read_csv("tests/data/dates.csv")
        cols_to_convert = ["date_1", "date_2", "date_3", "date_4", "date_5"]
        format_precidence = ["%Y-%m-%d", "%d-%b-%y","%y-%m-%d", "%d-%m-%Y","%m-%d-%Y"]
        df2 = convert_pd_columns_to_date(df, cols_to_convert, format_precidence)

        date_cols1 = ["date_1", "date_2", "date_3", "date_4", "date_5"]
        should_all_be_equal =  df2.loc[0,date_cols1]
        test1 = all(should_all_be_equal == datetime.date(2017,7,21))

        self.assertTrue(test1, "If correct precidence is given, should correctly convert all dates to same value")

        date_cols2 = ["date_2", "date_3", "date_4", "date_5"]
        should_all_be_equal =  df2.loc[1,date_cols2]
        test2 = all(should_all_be_equal == datetime.date(2017,7,21))

        self.assertTrue(test1, "If correct precidence is given, should correctly convert all dates to same value")

        should_not_all_be_equal =  df2.loc[1,date_cols1]
        test3 = all(should_not_all_be_equal == datetime.date(2017,7,21))

        self.assertFalse(test3, "There's a null, so this should fail")

        should_all_be_equal =  df2.loc[2,date_cols1]
        test4 = all(should_all_be_equal == datetime.date(2011,9,6))
        self.assertTrue(test4, "If correct precidence is given, should correctly convert all dates to same value")


    def test_convert_pd_columns_to_date_2(self):
        """
        Check it fails if we incorrectly specify date types
        """
        df = pd.read_csv("tests/data/dates.csv")
        cols_to_convert = ["date_1", "date_2", "date_3", "date_4", "date_5"]
        # Last format specified incorrectly, expect a ValueError
        format_precidence = ["%Y-%m-%d", "%d-%b-%y","%y-%m-%d", "%d-%m-%Y","%b-%d-%Y"]
        with self.assertRaises(ValueError):
            df2 = convert_pd_columns_to_date(df, cols_to_convert, format_precidence)

    def test_convert_pd_columns_to_date_3(self):
        """
        Check it fails if we mix date types
        """
        df = pd.read_csv("tests/data/dates.csv")
        df.iloc[0,0] = df.iloc[0,1]
        cols_to_convert = ["date_1", "date_2", "date_3", "date_4", "date_5"]
        format_precidence = ["%Y-%m-%d", "%d-%b-%y","%y-%m-%d", "%d-%m-%Y","%m-%d-%Y"]
        # Last format specified incorrectly, expect a ValueError
        with self.assertRaises(ValueError):
            df2 = convert_pd_columns_to_date(df, cols_to_convert, format_precidence)

    def test_find_and_log_pd_date_parse_errors_1(self):
        dates = ['2017-01-01', '2017-13-01', '', '2017-09-01', None]
        col = pd.Series(dates)

        with self.assertLogs(level='INFO') as cm:
            find_and_log_pd_date_parse_errors(col)

        self.assertEqual(cm.output, ["INFO:datacleaningutils.dates:Failed to parse '' with format %Y-%m-%d",
                                     "INFO:datacleaningutils.dates:Failed to parse 'None' with format %Y-%m-%d",
                                     "INFO:datacleaningutils.dates:Failed to parse '2017-13-01' with format %Y-%m-%d"])


if __name__ == '__main__':
    unittest.main()
