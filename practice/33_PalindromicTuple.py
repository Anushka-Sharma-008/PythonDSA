'''
33_PalindromicTuple.py
Palindromic Tuple
Check if Tuple is Palindromic

Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads the same forwards and backwards.

Parameters:

tup (tuple): The input tuple that you need to check for palindromic property.

Returns:

True if the tuple is palindromic, False otherwise.

Example:

Input: (1, 2, 3, 2, 1)
Output: True

Input: ('a', 'b', 'c', 'b', 'a')
Output: True

Input: (1, 2, 3, 4, 5)
Output: False

Input: ('x', 'y', 'z', 'x')
Output: False

Input: ('a',)
Output: True
'''

## SOLUTION

def is_palindromic_tuple(tup):
    if tup == tup[::-1]:
        return True
    else:
        return False

print(is_palindromic_tuple(('x', 'y', 'z', 'x')))