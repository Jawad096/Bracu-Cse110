"""Task 6
Write a Python program that reads 5 numbers into a list and prints the largest number and its location or index position on the list. [You are not allowed to use the max(), sort(), sorted() function here]

Hint: Assume the first input to be the largest value initially and the largest values location to be 0.

Note: You may need to be careful while printing the output. Depending on your code, you might need data conversion.

===================================================================

Sample Input:
7, 13, 2, 10, 6

Sample Output:
My list: [7, 13, 2, 10, 6]
Largest number in the list is 13 which was found at index 1."""

l = []
index_num = 0
lar_num = 0
for i in range(5):
    num = int(input("Enter five numbers: "))
    l.append(num)
for j in range(len(l)):
    if l[j]>lar_num:
        lar_num = l[j]
        index_num = j 
        



print("My list: ",l)
print("Largest number in the list is", lar_num, "which was found at index", index_num)