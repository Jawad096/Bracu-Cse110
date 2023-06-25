"""Task 12
Write a Python program that turns every item of a list into its square.

===================================================================

Sample Input 1:
[1, 2, 3, 4, 5, 6, 7]

Sample Output 1:
[1, 4, 9, 16, 25, 36, 49]

===================================================================

Sample Input 2:
[3, 5, 1, 6]

Sample Output 2:
[9, 25, 1, 36]"""

l = input("Create a list: ").split(",")
new_list = []
for i in l:
    new_list.append(int(i))
for j in range(len(new_list)):
    new_list[j] = new_list[j]**2
print(new_list)