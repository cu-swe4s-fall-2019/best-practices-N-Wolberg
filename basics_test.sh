#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# Test Basic Function

# Generate Temp File
(for i in `seq 1 1000`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

# PEP8 style 
run test_pep8_style pycodestyle style.py
assert_exit_code 0
run test_pep8_get_column_stats pycodestyle get_column_stats.py 
assert_exit_code 0

# Test
run test_normal python get_column_stats.py --file data.txt --column 3
assert_exit_code 0
assert_in_stdout 'mean:'
assert_in_stdout 'stdev:'

# Test errors
run err_no_inputs python get_column_stats.py
assert_in_stderr 'arguments are required'
assert_exit_code 2

run err_no_file python get_column_stats.py --file nofile --column 0
assert_in_stdout 'Location nofile invalid'
assert_exit_code 1

run err_bad_column python get_column_stats.py --file data.txt --column 10
assert_in_stdout 'Column number 10 exceeds file index'
assert_exit_code 1

for ((i=1;i<=10;i++));
do
    echo -e "a\tb\tc";
done > badfile.txt

run err_noninteger python get_column_stats.py --file badfile.txt --column 1
assert_in_stdout 'badfile.txt values must be integers; Confirm TSV formating'
assert_exit_code 1

chmod -rwx data.txt

run err_permissions python get_column_stats.py --file data.txt --column 0
assert_in_stdout 'Failed to open data.txt; Permissions Error'
assert_exit_code 1


# File Clean-up
chmod +rwx data.txt
rm data.txt
rm badfile.txt