"""Task 9
Write a Python program that reads 10 numbers into a list and prints the numbers of that specified list after removing even numbers from it.

=========================================================================

Sample Input:

7,12,4,55,96,2,11,61,33,42

Sample Output:

[7, 55, 11, 61, 33]"""

l = []
new_l = []
for i in range(10):
    num = int(input("Enter ten Numbers: "))
    l.append(num)
for j in l:
    if j % 2 !=0:
        new_l.append(j)
print(l)
print(new_l)