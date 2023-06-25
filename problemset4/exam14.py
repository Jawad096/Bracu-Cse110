"""Task 14
Write a Python program that takes two lists as an input from the user. Then print a new list with the common elements of both the input lists.

Hint: You may need to create a third list to store the results. You can use membership operators (in, not in) to make sure similar elements are added.

===================================================================

Sample Input 1:
A, B, C, D

C, E , F, B

Sample Output 1:
['C', 'B']

===================================================================

Sample Input 2:
1, 3, A, H, P

A, G, 1, P, O

Sample Output 2:
['1', 'A', 'P']"""

list_1 = input("List one: ").split(",")
list_2 = input("List two: ").split(",")
list_3 = []

for i in list_1:
    for j in list_2:
        if i==j :
            list_3.append(j)

print(list_3)