'''
57_InsertionSort.py
Insertion Sort
Insertion Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Insertion Sort algorithm. Insertion Sort works by building a sorted section of the list, one element at a time, by inserting each new element into its proper position within the already sorted section.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]

Input: lst = [31, 41, 59, 26, 41, 58]
Output: [26, 31, 41, 41, 58, 59]
'''

## SOLUTION

def insertion_sort(arr):
    n = len(arr)

    for current in range(1,n):
        currentCard = arr[current]
        correctPosition = current-1 # It will go from i-1 to 0
        while correctPosition >=0:
            if(arr[correctPosition] < currentCard):
                break
            else:
                arr[correctPosition +1 ] = arr[correctPosition]
                correctPosition-=1
            arr[correctPosition + 1] = currentCard

    return arr