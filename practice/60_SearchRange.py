'''
60_SearchRange.py
Find First and Last Position of Element in Sorted Array
Asked in companies

Goldman sachs

Amazon

Wipro

Airtel



Description:
Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1].



Parameters:

nums (List[int]): A list of integers sorted in non-decreasing order.

target (int): The target value to search for.

Return Values:

List[int]: The starting and ending positions of the target value in the array. If the target is not found, return [-1, -1].



Example:

Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
Explanation: The target 8 appears from index 3 to index 4.
 
 
Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
Output: [-1, -1] 
Explanation: The target 6 is not found in the array.
'''

## SOLUTION

def searchRange(nums, target):
    def findFirst(nums, target):
        size = len(nums)
        start = 0
        end = size - 1
        index = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return index
    def findLast(nums, target):
        size = len(nums)
        start = 0
        end = size - 1
        index = -1
        while start <= end :
            mid = (start + end) // 2
            if nums[mid] == target:
                index = mid
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return index
    
    first = findFirst(nums, target)
    last = findLast(nums, target)
    return [first, last]

print(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 10))