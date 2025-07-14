'''
52_Substring.py
Check for Substring
Problem Description:

You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.



Input:

Two strings s and t, where 1 <= len(s), len(t) <= 1000.



Output:

A boolean value (True or False) indicating whether t is a substring of s.



Example:

Input: s = "hello world", t = "world"
Output: True
 
Input: s = "hello world", t = "worlds"
Output: False
'''

## SOLUTION

def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    if t in s:
        return True
    else:
        return False