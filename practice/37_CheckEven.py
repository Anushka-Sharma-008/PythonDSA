'''
37_CheckEven.py
Check for Even Number
Problem Description:

You are given an integer n. Your task is to check whether the number is even or not. Return True if the number is even, and False otherwise.



Input:

A single integer n where -10^9 <= n <= 10^9.



Output:

Return True if n is an even number, otherwise return False.



Example:

Input: n = 4
Output: True
 
Input: n = 7
Output: False
'''

## SOLUTION

def is_even(n):
    """
    Function to check if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    bool = True
    if n % 2 !=  0:
        bool = False
    return bool

print(is_even(7))
