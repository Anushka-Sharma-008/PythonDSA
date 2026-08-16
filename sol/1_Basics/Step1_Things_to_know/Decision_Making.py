'''
DECISION MAKING
Given two integers, n and m. The task is to check the relation between n and m. Print "less" if n < m,  "equal" if n == m, and "greater" if n > m.

Examples :
Input: n = 4, m = 8
Output: lesser
Explanation: 4 < 8 so print 'less'.
Input: n = 8, m = 8
Output: equal
Explanation: 8 = 8 so print 'equal'.
Input: n = 8, m = 4
Output: greater
Explanation: 8 > 4 so print 'greater'.

Constraints:
-109 <= m , n <= 109
'''

n = int(input())
m = int(input())

# code here
if (n<m):
    print("less")
elif (n>m):
    print("greater")
else:
    print("equal")

# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)