# best-practices

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