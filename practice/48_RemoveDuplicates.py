'''
48_RemoveDuplicates.py
Remove Duplicates in a string
Problem Description:

You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.



Input:

A single string s, where the length of s is between 1 and 1000.



Output:

A string that contains only the first occurrence of each character from the input string.



Example:

Input: "programming"
Output: "progamin"
 
Input: "Hello, World!"
Output: "Helo, Wrd!"
'''

## SOLUTION

def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    new = ""
    for i in s:
        if i not in new:
            new += i
    return new

print(remove_duplicates("Hello, World!"))