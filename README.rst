.. image:: https://travis-ci.org/moj-analytical-services/datacleaningutils.svg?branch=master
    :target: https://travis-ci.org/moj-analytical-services/datacleaningutils

.. image:: https://codecov.io/gh/moj-analytical-services/datacleaningutils/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/moj-analytical-services/datacleaningutils


Data cleaning utilities
=========================
Unit tested functions for cleaning data as part of ETL processes.

* Dates
   * ``convert_pd_columns_to_date`` - Attempt conversion of column(s) to ``datetime.date`` using provided ``strptime`` formats


Contributing
------------

PRs will be accepted if:
1. Travis is passing, which means that your unit tests should pass, and pylint shouldn't be throwing warnings or errors.
2. Your function is appropriately unit tested
3. Your function has a docstring in `Google format <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_