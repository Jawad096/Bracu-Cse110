"""Task 1
Write a Python program that reads 10 numbers from the user into a list. After reading each number, print all the numbers that have been entered so far in the list.

Example:
After the user enters 3, prints “Numbers in the list: [3]”
After the user enters 5, prints “Numbers in the list: [3, 5]”
After the user enters 34, prints “Numbers in the list: [3, 5, 34]”
.... and so on"""
list = []
for n in range(10):
    x = int(input("Enter some values: "))
    list.append(x)
    print(list)