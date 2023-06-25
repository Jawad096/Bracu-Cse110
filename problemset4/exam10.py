"""Task 10
Write a Python program that removes all Empty strings from a given list and print the new list.

=========================================================================

Sample Input:

["hey", "there", " ", "what's", " ", "up", " ", "?"]

Sample Output:

Original List: ["hey", "there", " ", "what's", " ", "up", " ", "?"]

Modified List: ["hey", "there", "what's", "up", "?"]"""

l = ["hey","there"," ","what's", " ", "up", " ", "?"]
l_1 = []
for i in l:
    if i != " ":
        l_1.append(i)
print(l_1)
