'''
Created on Aug 22, 2017

@author: Alexandre F. Rosa
@note: Test Case module. In this module I tried to test all possible scenarios.  

'''
import unittest
import solution.array_list as al

#global variable
basic_input_array_list = [[1,2,[3]],4]
#global variable
complex_input_array_list = [[1,2,[3], 4],5, [6,7],[8,[9],10]]

class Test(unittest.TestCase):
    # a simple test using the parameters that are gave to me
    def test_flattening_demo_array(self):
        expected_array_list = [1,2,3,4] 
        global basic_input_array_list
        #invoking the method created in python module - solution.array_list.flattening_array
        list_flattened = al.flattening_array(basic_input_array_list)
        self.assertSequenceEqual(list_flattened, expected_array_list,"Array was flattened with success") 
    #a little be more complex test, now using a new structure of array.    
    def test_flattening_complex_array(self):
        expected_array_list = [1,2,3,4,5,6,7,8,9,10] 
        global complex_input_array_list
        list_flattened = al.flattening_array(complex_input_array_list)
        self.assertSequenceEqual(list_flattened, expected_array_list,"A complex array structure was flattened with success") 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()