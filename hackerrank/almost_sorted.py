#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def check_swap(arr, i, j):
    """
    Check if the array is sorted when swapping the indices i and j in the array.
    """
    new_arr = arr.copy()
    new_arr[i], new_arr[j] = new_arr[j], new_arr[i]
    return new_arr == sorted(arr)

def check_reverse(arr, i, j):
    """
    Check if the array is sorted when reversing the numbers between indices i and j in the array.
    """
    new_arr = arr.copy()
    new_arr[i:j+1] = new_arr[i:j+1][::-1]
    return new_arr == sorted(arr)

def almostSorted(arr):
    """
    Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.
    1. Swap two elements.
    2. Reverse one sub-segment.
    
    Determine whether one, both or neither of the operations will complete the task. Output is as follows.
    
    1. If the array is already sorted, output yes on the first line. You do not need to output anything else.
    2. If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:
        If elements can only be swapped, output the indices of the elements to be swapped.
        If elements can only be reversed, for the segment , output the indices of the first and last elements of the subarray to be reversed.
    3. If an array can be sorted both ways, by using either swap or reverse, choose swap.
    
    If the array cannot be sorted either way, output no on the first line.
    
    Example:
    Input:
    [4, 2]
    
    Output:
    yes  
    swap 1 2
    """
    
    # check if array is already sorted
    if arr == sorted(arr):
        print("yes")
        return
    
    # check if array can be sorted by swapping or reversing
    reverse_sol = [False, -1, -1]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Make sure the two indices are not sorted towards each other
            if arr[j] < arr[i]:
                # check if array can be sorted by swapping
                if check_swap(arr, i, j):
                    print("yes")
                    print("swap", i+1, j+1)
                    return
                # check if array can be sorted by reversing
                if not(reverse_sol[0]) and check_reverse(arr, i, j):
                    reverse_sol = [True, i, j]
    
    # Only print reverse solution after having made sure there is no preferred swap
    if reverse_sol[0]:
        print("yes")
        print("reverse", reverse_sol[1]+1, reverse_sol[2]+1)
        return

    # if array cannot be sorted by either swapping or reversing
    print("no")
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
