'''
65_PalindromeList.py
Palindrome List
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.



Input Parameters:

lst (List[int]): A list of integers.

Output:

bool: Return True if the list is a palindrome, otherwise False.



Example:

Input: lst = [7, 8, 9, 8, 7]
Output: True
 
Input: lst = [1, 2, 3, 4, 5]
Output: False
 
Input: lst = [1, 2, 3, 2, 1]
Output: True

'''

## SOLUTION

def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    if lst == lst[::-1]:
        return True
    else:
        return False