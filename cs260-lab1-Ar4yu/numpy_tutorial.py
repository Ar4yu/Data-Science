'''
Description: intro to numpy and it's functions
Author: Aaryaman Jaising
Date: January 21, 2025s
'''

# Some examples below are from Numpy's Quickstart tutorial:
# https://numpy.org/doc/stable/user/quickstart.html

import numpy as np
import random
import sys

################################################################################
# MAIN
################################################################################

def main():
    # NOTE: make sure to run the code frequently and analyze all output before
    # doing the TODO sections

    print("Array Initialization\n")

    # arrays of zeros, 1D array/vector
    ex_array_1d = np.zeros((5))
    print("1D array (of zeros)")
    print(ex_array_1d)
    print("shape:", ex_array_1d.shape, "\n")

    # fill with random numbers
    for i in range(ex_array_1d.shape[0]):
        ex_array_1d[i] = random.randrange(0, 101)
    print("1d array (filled with random numbers)")
    print(ex_array_1d, "\n")

    # 2-D array initialized with random numbers
    print("2D array of random numbers")
    ex_array_2d = np.random.rand(5, 4)
    print(ex_array_2d, "\n")
    print("shape:", ex_array_2d.shape, "\n")

    ### ========== TODO 1 : START ========== ###

    # Create a 3D array of zeros with shape (4,6,5)

    # Fill the array with random values from [0, 301)

    # Print out the array and its shape
    arr_3d = np.zeros((4,6,5))
    print(arr_3d.shape)
    for x in range(arr_3d.shape[0]):
        for y in range(arr_3d.shape[1]):
            for z in range(arr_3d.shape[2]):
                arr_3d[x][y][z] = random.randrange(301)
    
    print(arr_3d)
    print(arr_3d.shape)
    ### ========== TODO 1 : END ========== ###
    #sys.exit("finish TODO 1") # comment to continue lab

    # array from a list
    fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    fib_array = np.array(fib_list)
    print("fibonacci list")
    print(fib_list, type(fib_list))
    print("np array from fib list")
    print(fib_array, type(fib_array), "\n")

    # array from a range: (start, stop, step)
    ex_array_from_range_a = np.arange(10) # stop
    ex_array_from_range_b = np.arange(0, 2, 0.3) # start, stop, step
    print("1d array from a range (10)")
    print(ex_array_from_range_a)
    print("1d array from a range (0, 2, 0.3)")
    print(ex_array_from_range_b, "\n")

    # array from linspace: (start, stop, num points)
    ex_array_from_linespace = np.linspace(5, 10, 20) # start, stop, num points
    print("1d array from a linspace (5, 10, 20)")
    print(ex_array_from_linespace)

    print("Sorting\n")

    # sort
    ex_array_1d_sorted = np.sort(ex_array_1d)
    print("the sorted array")
    print(ex_array_1d_sorted, "\n")

    ### ========== TODO 2 : START ========== ###

    print("Array Slicing\n")

    # Read the section 'Basic Slicing and Indexing' of a page from the numpy
    #documentation (https://numpy.org/doc/stable/reference/arrays.indexing.html)
    ex_array_2d = np.array([[30, 68, 20, 39],
                            [82, 58, 55, 91],
                            [23, 68, 78, 40],
                            [18, 34, 25, 76],
                            [53, 73,  5, 32]])
    print("2d array (filled with random numbers)")
    print(ex_array_2d, "\n")
    # For the commented out examples of array slicing, write out the expected
    # output in your README.
    '''
    print("ex_array_2d[2]")
    print(ex_array_2d[2], "\n")

    print("ex_array_2d[:,1]")
    print(ex_array_2d[:,1], "\n")

    print("ex_array_2d[:3,:2]")
    print(ex_array_2d[:3,:2], "\n")

    print("ex_array_2d[2:4,:]")
    print(ex_array_2d[2:4,:], "\n")
    '''

    # Comment the code back in and check your answer against the actual output.

    ### ========== TODO 2 : END ========== ###
    # sys.exit("finish TODO 2") # comment to continue lab

    ### ========== TODO 3 : START ========== ###
    
    # go through the following code: make sure it makes sense and answer README
    # question

    print("Array Concatenation\n")

    # concatenation
    print("2d array (main one in the concatenation examples) (5x4)")
    print(ex_array_2d, "\n")
    to_be_concat = np.arange(2, 10, 2)
    to_be_concat = np.reshape(to_be_concat, (1,4))
    print("array (to be concatenated to the 2d array) (1x4)")
    print(to_be_concat)
    print("After concatenation (axis=0) (6x4)")
    print(np.concatenate((ex_array_2d, to_be_concat), 0), "\n")

    # Note: see official concatenation documentation to understand the next part
    #(https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)

    # README: explain why the following code throws an error
    try:
        print("2d array with the above array concatenated to it (axis=1)")
        print(np.concatenate((ex_array_2d, to_be_concat), 1), "\n")
    except ValueError:
        print("cannot concatenate arrays")

    to_be_concat_2 = np.arange(5)
    to_be_concat_2 = np.reshape(to_be_concat_2, (5,1))
    print("array (to be concatenated to the 2d array) (5x1)")
    print(to_be_concat_2)
    print("After concatenation (axis=1) (5x5)")
    print(np.concatenate((ex_array_2d, to_be_concat_2), 1), "\n")

    print("Basic Operations\n")

    a = np.arange(4)
    b = np.arange(3, 11, 2)

    print("vector a")
    print(a)
    print("vector b")
    print(b, "\n")

    # Basic Operations
    # elementwise
    # +
    print("a + 2")
    print(a + 2)
    print("a + b")
    print(a + b, "\n")

    # -
    print("a - 7")
    print(a - 7)
    print("b - a")
    print(b - a, "\n")

    # **, exponents -> x^y
    print("b**2 (b^2)")
    print(b**2, "\n")

    # *, multiplication
    print("a * 0.5")
    print(a * 0.5)
    print("a * b")
    print(a * b, "\n")

    ### ========== TODO 3 : END ========== ###

if __name__ == "__main__":
    main()
