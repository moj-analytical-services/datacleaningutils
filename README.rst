.. image:: https://travis-ci.org/moj-analytical-services/datacleaningutils.svg?branch=master
    :target: https://travis-ci.org/moj-analytical-services/datacleaningutils

.. image:: https://codecov.io/gh/moj-analytical-services/datacleaningutils/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/moj-analytical-services/datacleaningutils


Data cleaning utilities
=========================
Unit tested functions for cleaning data as part of ETL processes.

* dates
   * ``convert_pd_columns_to_date`` - Attempt conversion of column(s) to ``datetime.date`` using provided ``strptime`` formats
* data_types
   * ``rough_heuristic_pd_column_type_check`` - A very quick heuristic/rule of thumb that checks the data type of a column in pandas
* structure
   * ``check_compatible_with_metadata`` - Checks compatibility with metadata as specified in the format in https://github.com/moj-analytical-services/data_warehouse_database_template


Contributing
------------

PRs will be accepted if:
1. Travis is passing, which means that your unit tests should pass, and pylint shouldn't be throwing warnings or errors.
2. Your function is appropriately unit tested
3. Your function has a docstring in `Google format <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_