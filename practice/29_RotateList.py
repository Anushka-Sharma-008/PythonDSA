'''
29_RotateList.py
Rotate a List
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

Parameters:

lst (List of integers): The list to be rotated.

k (Integer): The number of positions to rotate the list.

Returns:

A list of integers rotated by k positions.

Example:

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
'''

## SOLUTION

def rotate_list(lst, k):
    n = len(lst)

    # If list is empty, return as is
    if n == 0:
        return lst

    # If k is more than length, we rotate only the remainder times
    k = k % n

    # Repeat k times: move last element to front
    for _ in range(k):
        last = lst.pop()       # remove last element
        lst.insert(0, last)    # add it to the beginning

    return lst
