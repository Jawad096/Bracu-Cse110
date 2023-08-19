"""Task 5
Write a python program that takes an input from the user and finds the number of times that the input is present in a given tuple.

===================================================================

Example 1:

Given tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

Sample Input 1:

8

Sample Output 1:

8 appears 4 times in the tuple

===================================================================

Example 2

Given tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

Sample Input 2:

1

Sample Output 2:

1 appears 0 times in the tuple"""

Given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
user_input = int(input("Enter a number: "))
l = 0
for i in Given_tuple:
    if i == user_input:
        l += 1
print(user_input,"appears",l,"times in the tuple")