'''
70_IsArraySorted.py

Is Array Sorted?
Asked in Companies:

Google

Microsoft

Amazon

Facebook



Description:
Write a function that checks whether the given array is sorted in non-decreasing order. The array is considered sorted if every element is less than or equal to the next element.



Input Parameters:

arr (List[int]): A list of integers.

Output:

bool: True if the array is sorted in non-decreasing order, False otherwise.



Example:

Input: arr = [5, 4, 3, 2, 1]
Output: False
 
Input: arr = [1, 3, 2, 4, 5]
Output: False
 
Input: arr = [1, 2, 3, 4, 5]
Output: True

'''

## SOLUTION

def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    if arr == sorted(arr):
        return True
    else:
        return False
