'''
WHILE LOOP
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.

Example:
Input: x = 3
Output: 3 2 1 0
Explanation: Numbers in decreasing order from 3 are 3 2 1 0.

Input: x = 5
Output: 5 4 3 2 1 0
Explanation: Numbers in decreasing order from 5 are 5 4 3 2 1 0.

Constraints:
0 ≤ x ≤ 100
'''

class Solution:
    def utility(self, x):
        # code here
        n = x
        while (n >= 0):
            print(n,end =" ")
            n = n - 1

# Time Complexity: O(x)
# Auxiliary Space Complexity: O(1)