"""Task 8
Write a Python program that takes two lists and prints True if they have at least one common member.

===================================================================

Sample Input 1:
List_one : [1, 4, 3, 2, 6]
List_two : [5, 6, 9, 8, 7]

Sample Output 1:
True

===================================================================

Sample Input 2:
List_one : [1, 4, 3, 2, 5]
List_two : [8, 7, 6, 9]

Sample Output 2:
False"""

l_one = input("List One: ").split(",")
l_two = input("List Two: ").split(",")
c = 0

for i in l_one:
    for j in l_two:
        if i == j:
            c += 1 

if c>0:
    print("True")
else:
    print("False")