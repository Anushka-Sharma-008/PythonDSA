'''
61_MinimumInRotatedSortedArray.py

Minimum in Rotated Sorted Array
Asked in companies

Google

Arcesium

Phone Pe

Qualcomm



Description:
Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot.



Parameters:

nums (List[int]): A list of integers sorted in ascending order but rotated at an unknown pivot.

Return Values:

int: The minimum element in the rotated sorted array.



Example:

Input: nums = [4, 5, 6, 7, 0, 1, 2] 
Output: 0 
Explanation: The minimum element is 0.
 
Input: nums = [11, 13, 15, 17] 
Output: 11 
Explanation: The array was not rotated, and the minimum element is the first element.
'''

## SOLUTION

def findMin(nums):
    return min(nums)

# def findMin(self, nums):
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[right]:
#                 # Minimum is in the right half
#                 left = mid + 1
#             else:
#                 # Minimum could be at mid or in the left half
#                 right = mid
#         return nums[left]    