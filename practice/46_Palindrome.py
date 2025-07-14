'''
46_Palindrome.py
Check Palindrome
Problem Description:

You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.



Input:

A single string s, where the length of s is between 1 and 1000.



Output:

A boolean value: True if the string is a palindrome, and False otherwise.



Example:

Input: "A man a plan a canal Panama"
Output: True
 
Input: "Hello, World!"
Output: False
'''

## SOLUTION

def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
    
print(is_palindrome("A man a plan a canal Panama"))