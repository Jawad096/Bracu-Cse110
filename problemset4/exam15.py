"""Task 15
Write a Python program that reads 5 numbers into a list and prints the second largest number and its location or index position on the list. [You are not allowed to use the max(), sort(), sorted() function here]

===================================================================

Sample Input:
7, 13, 2, 10, 6

Sample Output:
My list: [7, 13, 2, 10, 6]
Second largest number in the list is 10 which was found at index 3."""

l = input("Enter a list of numbers: ").split(",")
my_list = []
lar_num = 0
sec_lar_num = 0
index_num = 0
sec_lar_index = 0
for i in l:
    my_list.append(int(i))
for j in range(len(my_list)):
    if my_list[j]> lar_num:
        lar_num = my_list[j]
        index_num = j
    elif my_list[j]> sec_lar_num:
        sec_lar_num= my_list[j]
        sec_lar_index = j

print(my_list)
print("largest num of the list is ",lar_num,"which is in index ",index_num)
print("Second large num is ",sec_lar_num, "which is in index ",sec_lar_index)