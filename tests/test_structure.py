# -*- coding: utf-8 -*-

"""
Tests
"""
import datetime
import unittest
import pandas as pd
from datacleaningutils.structure import check_compatible_with_metadata

class StructureTest(unittest.TestCase):
    """
    Test the structure functions
    """

    def test_check_compatible_with_metadata_1(self):
        """
        Check it fails if we incorrectly specify date types
        """

        data = {
            'field_1': ["a", "b"],
            'field_2': ["a", "b"],
            'field_3': ["a", "b"]
        }
        df = pd.DataFrame(data)
        df = df[["field_1", "field_2", "field_3"]]

        check_compatible_with_metadata(df, "tests/data/meta1.json")

    def test_check_compatible_with_metadata_2(self):
        """
        Check it fails if we incorrectly specify date types
        """

        data = {
            'field_1': ["a", "b"],
            'field_2': ["a", "b"],
            'field_3': ["a", "b"],
            'field_4': ["a", "b"]
        }

        df = pd.DataFrame(data)
        df = df[["field_1", "field_2"]]
        with self.assertRaises(ValueError):
            check_compatible_with_metadata(df, "tests/data/meta1.json")


        df = pd.DataFrame(data)
        df = df[["field_1", "field_2", "field_3", "field_4"]]
        with self.assertRaises(ValueError):
            check_compatible_with_metadata(df, "tests/data/meta1.json")


        df = pd.DataFrame(data)
        df = df[["field_2", "field_1", "field_3"]]
        with self.assertRaises(ValueError):
            check_compatible_with_metadata(df, "tests/data/meta1.json")

if __name__ == '__main__':
    unittest.main()
