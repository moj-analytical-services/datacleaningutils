from setuptools import setup

# see https://stackoverflow.com/questions/14399534/reference-requirements-txt-for-the-install-requires-kwarg-in-setuptools-setup-py
setup(name='datacleaningutils',
      version='0.0.1',
      description='Functions for cleaning data as part of ETL processes',
      url='https://github.com/RobinL/python_package_template',
      author='Robin Linacre',
      author_email='robinlinacre@hotmail.com',
      license='MIT',
      packages=['datacleaningutils'],
      setup_requires=['pandas'],
      test_requires=["pylint", "coverage", "codecov"],
      zip_safe=False)
