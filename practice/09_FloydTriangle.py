'''
09_FloydTriangle.py
Floyds Triangle
Problem Description:

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in Floyd's Triangle.



Example:

Input: 5
Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
 
Input: 3
Output: ['1', '2 3', '4 5 6']
'''

## SOLUTION

def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    triangle = []
    current = 1

    for row in range(1, n + 1):
        line = []
        for _ in range(row):
            line.append(str(current))
            current += 1
        triangle.append(' '.join(line))

    return triangle

print(generate_floyds_triangle(5))

