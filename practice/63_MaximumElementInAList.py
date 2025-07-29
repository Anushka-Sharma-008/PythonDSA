'''
63_MaximumElementInAList.py
Maximum Element in a List.
Asked in Companies:

Google

Amazon

Microsoft

Facebook



Description:
Given a list of integers, write a function to find the maximum element in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The maximum element in the list.



Example:

Input: lst = [3, 5, 2, 9, 6]
Output: 9
 
Input: lst = [-1, -2, -3, -4]
Output: -1
 
Input: lst = [7]
Output: 7
'''

## SOLUTION

def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    if not lst:
        return -1
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum