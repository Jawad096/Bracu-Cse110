"""Task 2
Assume, you have been given a tuple. Write a Python program that creates a new tuple excluding the first and last two elements of the given tuple and prints the new tuple.

Hint: You may use tuple slicing.

===================================================================

Sample Input 1:
(10, 20, 24, 25, 26, 35, 70)

Sample Output 1:
(24, 25, 26)

===================================================================

Sample Input 2:
(-10, 20, 30, 40)
Sample Output 2:
()

===================================================================

Sample Input 3:
(-10, 20, 25, 30, 40)

Sample Output 3:
(25,)"""

user_tuple = input("Enter tuples and put space after each value :").split()
user_tuple=tuple((user_tuple))
length = len(user_tuple)
new_tuple = user_tuple[2:(length-2)]
print(new_tuple)