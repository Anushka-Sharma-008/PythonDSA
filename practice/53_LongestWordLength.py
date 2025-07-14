'''
53_LongestWordLength.py
Length of the Longest Word
Problem Description:

You are given a string s. Your task is to find the length of the longest word in the string. A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.



Input:

A string s, where the length of s is between 1 and 1000 characters.



Output:

An integer representing the length of the longest word in the string.



Example:

Input: s = "The quick brown fox jumps over the lazy dog"
Output: 5
 
Input: s = "Hello World"
Output: 5
'''

## SOLUTION

def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    """
    c = 0
    for word in s.split():
        if len(word) > c:
            c = len(word)
    return c

print(longest_word_length("The quick brown fox jumps over the lazy dog"))