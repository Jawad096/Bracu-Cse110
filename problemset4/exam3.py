"""Task 3
Write a python program that reads 5 numbers from the user into a list, and then prints them in the reverse order.

Hint: You may create a list to store the input numbers and then use loop to print them in reverse order

===================================================================

Sample Input:
5
-5
100
1
0"""
user_list = []
for i in range(5):
    num = int(input("enter numbers: "))
    user_list.append(num)
#user_list.reverse()
list_2 = user_list[::-1]
for j in list_2:
#print(user_list)
    print(j)