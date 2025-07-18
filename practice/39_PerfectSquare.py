'''
39_PerfectSquare.py
Valid Perfect Square
Problem Description:

You are given a positive integer num. Your task is to check whether num is a perfect square or not. A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.



Input:

A single positive integer num where 1 <= num <= 10^9.



Output:

Return True if num is a perfect square, otherwise return False.



Example:

Input: num = 16
Output: True
 
Input: num = 14
Output: False
'''

## SOLUTION

def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    import math
    
    if num < 0:
        return False
    
    root = math.isqrt(num)
    return root * root == num

print(is_perfect_square(1))