"""Task 5
Write a Python program that takes numbers as input into a list, removes multiple occurences of any number and then finally prints a list without duplicate values.

Hint: You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.

===================================================================

Sample Input 1:
0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4

Sample Output 1:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
n = input().split(",")
y = []
for i in n:
    if i not in y:
        y.append(i)
y = list(map(int, y))
print(y)        
#print(z)
'''x = []
for j in y:
    x.append(int(j))
print(x)
print(y)'''