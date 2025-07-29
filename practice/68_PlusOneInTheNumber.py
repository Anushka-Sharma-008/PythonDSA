'''
68_PlusOneInTheNumber.py

Plus One in the Number
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeroes.

Write a function to increment the large integer by one and return the resulting array of digits.



Input Parameters:

digits (List[int]): A list of integers where each integer represents a digit of a large number.

Output:

List[int]: The list representing the number after incrementing it by one.



Example:

Input: digits = [1, 2, 3]
Output: [1, 2, 4]
 
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
 
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]

'''

## SOLUTION

def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    n = len(digits)
    
    # Start from the last digit and process backwards
    for i in reversed(range(n)):
        if digits[i] < 9:
            digits[i] += 1
            return digits  # Done, return early
        else:
            digits[i] = 0  # Since it was 9, becomes 0 and continue
    
    # If we exited the loop, all the digits were 9 (e.g., [9, 9, 9]), we need to add a new digit at the front
    return [1] + [0]*n
