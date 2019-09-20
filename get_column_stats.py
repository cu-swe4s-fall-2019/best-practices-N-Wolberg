import sys
import math
import argparse


def parse_arguments():

    parser = argparse.ArgumentParser(description='Gives \
                                     mean and standard diviation \
                                     of given column of numbers \
                                     from provided TSV file')

    parser.add_argument('--file',
                        type=str,
                        help='TSV File location',
                        required=True)

    parser.add_argument('--column',
                        type=int,
                        help='Column to calculate',
                        required=True)

    args = parser.parse_args()

    return args


def get_values(file, column):

    """
    Returns the column specified from the TSV file as an array.

    Arguments
    ---------
    file : str
        location of TSV file
    column : int
        column to return

    Returns
    ---------
    values : int array
        values from specified column
    """

    file = open(file, 'r')
    values = []

    for data in file:
        temp_values = [int(value.strip()) for value in data.split()]
        values.append(temp_values[column])

    return values


def calc_mean(values):

    """
    Finds the mean from given array of integers,
    Returns if there is at least one number passed

    Arguments
    ---------
    values : numerical array
        array of integers or floats to calculate mean

    Returns
    ---------
    mean : float
        mean of given array
    """
    

    if type(values) != list:
            raise TypeError('Bad Argument, Requires list of numbers')
    if len(values) == 0:
        raise ZeroDivisionError('list is empty')
    
    s = []
    for i in values:
        if type(i) == int or float:
            s.append(i)
        else:
            print('Skipping bad index')
            continue
    if len(s) != 0:
        return sum(s)/len(s)
    else:
        raise TypeError('Bad Argument, Requires list of numbers') 
        


def calc_stdev(values, mean):

    """
    Finds the standard deviation of given array with its mean

    Arguments
    ---------
    values : int array
        array of integers to calculate standard diviation

    Returns
    ---------
    stdev : float
        standard deviation of given array
    """
    if mean == None:
        mean = calc_mean(values)
    
    if type(mean) == int or float:
        if type(values) == list:
            if len(values) == 0:
                raise ZeroDivisionError('list is empty')

            calc_array = []
            for i in values:
                if type(i) == int or float:
                    print(type(i))  #debug line
                    calc_array.append(i)
                else:
                    print('Skipping bad index')
                    continue
            if len(calc_array) == 0:
                raise TypeError('Bad Argument, Requires list of numbers')
                    
            stdev = math.sqrt(sum([(float(mean)-float(x))**2 for x in calc_array]) / len(calc_array))
            return stdev               
        else:
            raise TypeError('Bad Argument, Requires list of numbers')
    else:
        raise TypeError('Bad Second Argument: Use Number or None')




def main():

    args = parse_arguments()

    try:
        Values = get_values(args.file, args.column)
    except FileNotFoundError:
        print('Location ' + args.file + ' invalid')
        sys.exit(1)
    except PermissionError:
        print('Failed to open ' + args.file + '; Permissions Error')
        sys.exit(1)
    except ValueError:
        print(args.file + ' values must be integers; Confirm TSV formating')
        sys.exit(1)
    except IndexError:
        print('Column number ' + str(args.column) + ' exceeds file index')
        sys.exit(1)

    try:
        Mean = calc_mean(Values)
        print('mean:', Mean)
        StDev = calc_stdev(Values, Mean)
        print('stdev:', StDev)
    except ZeroDivisionError:
        print('Cannot divide by zero! Check file values and formating')
        sys.exit(1)
    except ValueError:
        print('Cannot calculate. Check file values and formating')
        sys.exit(1)


if __name__ == '__main__':
    main()
