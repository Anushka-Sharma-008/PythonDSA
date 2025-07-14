'''
40_DecimalToBinary.py
Decimal to Binary
Problem Description:

You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.



Input:

A single integer n, where -10^9 <= n <= 10^9.



Output:

A string representing the binary representation of n.



Example:

Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
'''

## SOLUTION

def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    if n == 0:
        return "0"
    
    is_negative = n < 0
    n = abs(n)
    
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    
    result = ''.join(reversed(binary))
    return '-' + result if is_negative else result

print(int_to_binary(-5))
