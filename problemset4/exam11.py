"""Task 11
Write a Python program that replaces the last element of first list with second list.

===================================================================

Sample Input 1:
List_one : [1, 4, 7, 5]
List_two : [6, 1, 3, 9]

Sample Output 1:
[1, 4, 7, 6, 1, 3, 9]

===================================================================

Sample Input 2:
List_one : [1, 3, 5, 7, 9, 10]
List_two : [2, 4, 6, 8]

Sample Output 2:
[1, 3, 5, 7, 9, 2, 4, 6, 8]"""

l_1 = input("List 1: ").split(",")
l_2 = input("List 2: ").split(",")
new_l = []

for i in range(len(l_1)-1):
    new_l.append(int(l_1[i]))
for j in l_2:
    new_l.append(int(j))

print(new_l)