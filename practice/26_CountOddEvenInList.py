'''
26_CountOddEvenInList.py
Count Number of Odd and Even Elements in a List
Count Even and Odd Numbers in a List

You are given a list of integers. Write a Python program that counts and returns the number of even and odd numbers in the list.

Parameters:

lst (List of integers): The list of integers where you will count the even and odd numbers.

Returns:

A tuple (even_count, odd_count) where even_count is the number of even numbers and odd_count is the number of odd numbers.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: (2, 3)

There are 2 even numbers: 2, 4

There are 3 odd numbers: 1, 3, 5
'''

## SOLUTION

def count_even_odd(lst):
  odd = 0
  even = 0
  for i in lst:
    if (i % 2) == 0:
      even += 1
    else:
      odd += 1
  return (even,odd)

print(count_even_odd([1, 2, 3, 4, 5]))