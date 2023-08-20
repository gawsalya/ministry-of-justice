# Ministry of justice
This repository contains my solution for the ministry of justice technical assessment code. 

# Data engineering Python tests

There are 3 directories in this directory:

- test_1
- test_2
- test_3

### Test 1

This function extracts and structures data from the file `sample.log`. By running `python3 test_1.py` the file will run.

- test_1.py - 2 functions to navigate through the sample log
- test_for_test_1.py -- tests to make sure that different possibilities for input are considered

### Test 2

Gets data from a court API and matches it with data from the file `people.csv`.

- test_2.py -- contains the main script to run the functions required to get data from API and return this information in a formatted way
- courts_functions.py -- individual functions for the process of extraction and formatting - test_courts_functions.py -- test for the functions to make sure edge cases are contained and functions work

### Test 3

- test_3.py - Contains a function to sum up the time.
- test_for_test_3.py - contains test to test this function.

# ministry-of-justice
