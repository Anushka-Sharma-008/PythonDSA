'''
WHILE LOOP
Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.

A number ends with digit d if its last digit is d.

Example 1
Input: d = 1
Output: 12300
Explanation:
The first 50 positive integers ending with 1 are: 1, 11, 21, 31, ..., 491
Their sum is 12300.

Example 2
Input: d = 5
Output: 12500
'''

class Solution:
    def whileLoop(self, d : int) -> int:
        # Your code goes here
        sum = 0
        c = 0
        num = d
        while c<50:
            sum += num
            num += 10
            c +=1
        return sum

# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)