"""Task 13
Write a Python program that reads 5 numbers into a list and prints the smallest and largest number and their locations in the list. [You are not allowed to use the max(), min(), sort(), sorted() functions here]

Hint: You may assume the first input to be the largest value initially and the largest value’s location to be 0. Similarly, you can assume the first input to be the smallest value initially and the smallest value’s location to be 0.

Note: You may need to be careful while printing the output. Depending on your code, you might need data conversion.

===================================================================

Sample Input:
7, 13, -5, 10, 6

Sample Output:
My list: [7, 13, -5, 10, 6]
Smallest number in the list is -5 which was found at index 2
Largest number in the list is 13 which was found at index 1"""

l = input().split(",")
l_1 = []
lar_num = 0
index_num = 0
small_num = 0
index_num_1 = 0

for i in l:
    l_1.append(int(i))

small_num = int(l[0])
for j in range(len(l_1)):
    if l_1[j] > lar_num:
        lar_num = l_1[j]
        index_num_1 = j
    if l_1[j] < small_num:
        small_num = l_1[j]
        index_num = j
print("My list: ", l_1)
print("Largest number in list is ", lar_num, "which was found at index ", index_num_1)
print("Smallest number in list is ", small_num, "which was found at index ", index_num)