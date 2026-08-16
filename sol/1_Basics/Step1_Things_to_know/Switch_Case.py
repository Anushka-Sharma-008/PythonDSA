'''
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

Ensure only the 1st letter of the answer is capitalised.

For printing use:-
for C++ : cout << variable_name;
for Java : System.out.print();
for Python : print()
for Javascript : console.log()

Example 1
Input: day = 3
Output: Wednesday

Example 2
Input: day = 8
Output: Invalid
'''

class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case _:
                print("Invalid")

# Time Complexity: O(1)
# Auxiliary Space Complexity: O(1)