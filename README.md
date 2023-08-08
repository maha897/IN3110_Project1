# Assignment 2 - Basic Python Programming
This directory contains code for my implementation of the Array Class. You can find the implementation in array_class.py. The code also contains some unit tests for the class, found in test_array.py. My array can be one- and two-dimensional, but n-dimensional arrays are not supported (for now).

## Running tests

To run tests for arrayclass.py, run following command:
```
pytest test_array.py
```
#### Test coverage

> pytest --cov-report term --cov=test_array
```
---------- coverage: platform win32, python 3.10.8-final-0 -----------
Name      |      Stmts  | Miss | Cover
-----------------------------------
test_array.py |     80  |   12  |  85%
-----------------------------------
TOTAL       |       80   |  12 |   85%
```
