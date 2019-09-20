import unittest
import get_column_stats as gcs
import random

class TestGetColumnStats(unittest.TestCase):
#(t)est, (r)esult, (e)xpectation

#Start with testing mean.
    #Test Failures & Exceptions
    def test_mean_empty_list(self):
        t = []
        with self.assertRaises(ZeroDivisionError) as context:
            gcs.calc_mean(t)
        self.assertEqual(str(context.exception), 'list is empty')

    def test_mean_null_list(self):
        with self.assertRaises(TypeError) as context:
            gcs.calc_mean(None)
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

    def test_mean_non_integer(self):
        with self.assertRaises(TypeError) as context:
            gcs.calc_mean('abc')
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')
        
    def test_mean_not_a_list(self):
        with self.assertRaises(TypeError) as context:
            gcs.calc_mean(652)
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

        with self.assertRaises(TypeError) as context:
            gcs.calc_mean(8.56)
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

    #test intended cases
    def test_mean_const_array(self):
        r = gcs.calc_mean([1])
        self.assertEqual(r, 1)
        
    def test_mean_float_list(self):
        t = [1.5, 5.985, 7.43]
        r = gcs.calc_mean(t)
        e = sum(t)/len(t)
        self.assertEqual(r, e)
    
#Testing StDev
    #Test Failures & Exceptions
    def test_stdev_empty_args(self):
        t = []
        with self.assertRaises(ZeroDivisionError) as context:
            gcs.calc_stdev(t, None)
        self.assertEqual(str(context.exception), 'list is empty')

    def test_stdev_null_list(self):
        with self.assertRaises(TypeError) as context:
            gcs.calc_stdev(None, 0)
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

    def test_stdev_non_number_list(self):
        t = ['a', 'b', 'c']
        with self.assertRaises(TypeError) as context:
            gcs.calc_stdev(t, 1)
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

    def test_stdev_non_number_mean(self):
        t = [1, 1, 1]
        g = gcs.calc_stdev(t, 'ghf')
        with self.assertRaises(TypeError) as context:
            gcs.calc_stdev(t, 'bad')
        self.assertEqual(str(context.exception), 'Bad Argument, Requires list of numbers')

    #Test Intended Cases
    def test_stdev_full(self):
        r = gcs.calc_stdev([3, 3, 5, 5], 4)
        self.assertEqual(r, 1)

if __name__ == '__main__':
  unittest.main()
