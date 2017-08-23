'''
Created on Aug 22, 2017

@author: Alexandre F. Rosa
@note: This module is a part of dev. hiring test. I used Python 2.7.x to solve this problem.  
@method: flattening_array
@param:  multidimensional array like: [[1,2,[3]],4] 
@output: a flattened array reshaped but, with the same order, like this: [1,2,3,4].
'''    

def flattening_array(array):
    result_array_list = {} 
    index = 0 
    for item in array:
        if isinstance(item, list):
            #using recursive approach to get any kind of sub array.
            aux = flattening_array(item)
            for temp in aux:
                result_array_list[index] = temp
                index = index +1
        else:
            result_array_list[index] = item
            index = index + 1
    #transforming a Python Dict in an output array
    return result_array_list.values()

        
arr = [[1,2,[3]],4] 
print flattening_array(arr)

