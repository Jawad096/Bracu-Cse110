"""Task 2
Write a Python program that takes a list as an input from the user.Then creates a new list excluding the first and last two elements of the given list and prints the new list. If there are not enough elements in the list to do the task, the print "Not possible".

Note: You may use list slicing.

===================================================================

Sample Input 1:
[10, 20, 24, 25, 26, 35, 70]
Sample Output 1:
[24, 25, 26]"""
new_list = []
lsize=int(input("Please enter list size"))
for i in range(lsize):
    num1=int(input("Please enter a number"))
    new_list.append(num1)

print(new_list[2:-2])