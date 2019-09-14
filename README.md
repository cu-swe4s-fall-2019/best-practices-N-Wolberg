# best-practices

## Description

An exercise in "best practices" for coding in python and hosting a repository.
`style.py` is simple example of PEP 8 styling 
`get_column_stats.py` is an example of "best practices" for a user-friendly interface with PEP 8 styling. 
`basics_test.sh` 

## Usage

Requirements: 
Python 3.6 installed 

`get_column_stats.py` will take a Tab-Separated-Values file (TSV) and a column of user's choice 
and returns the mean of the column with its standard diviation. 

```
python get_column_stats.py --file [file_name] --column [column_number]
```


## Testing

A premade code tester for `get_column_stats.py` - comes with bash code to handle required packages.

Requires pycodestyle to verify PEP 8 styling

```
pip install pycodestyle
```


Run test script with:

``` 
./basics_test.sh
```

All functional tests should be passed. 


# Update History:

Edit 9/13 11:00pm - Put instructions in README

Edit 9/13 10:30pm - Make basic_test.sh more exhaustive
- added SSSHtest to verify the behavior of code.
- test for normal functionality with random numbers
- test for exception when forcing bad input
- correct small syntax errors in get_column_stats.py

Edit 9/13 9:00pm - Overhaul get_column_stats.py
- Separated functions & added main().
- Parse arguments as a function.
- Add documentation to functions.
- Handle general errors.
- format to pycodestyle.


Edit 9/13 1:10pm - Fix style errors in style.py according to pycodestyle
- removed/added whitespace/indentation.
- rename bad variables (I, O, k, l) by adding "var_" in front.
- added exception AssertionError to except (line 113).
- added main() function.