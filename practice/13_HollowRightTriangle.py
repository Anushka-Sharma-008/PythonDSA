'''
13_HollowRightTriangle.py
Hollow Right Triangle
Problem Description:

You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be right-aligned.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the hollow right-angled triangle.



Example:

Input: 4
Output: ['*', '**', '* *', '****']
 
Input: 5
Output: ['*', '**', '* *', '*  *', '*****']
'''

## SOLUTION

def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    triangle = []
    for i in range (1, n+1):
        if (i == 1) or (i == n):
            triangle.append('*' * i)
        else:
            spaces = ' ' * (i-2)
            triangle.append('*' + spaces + '*')
    return triangle

print(generate_hollow_right_angled_triangle(6))