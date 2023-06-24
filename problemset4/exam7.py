"""Task 7
Assume, you have been given two lists. [Your program should work for any two given lists; make changes to the lists below and check whether your program works correctly]

list_one = [1, 2 , 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]

Write a Python program that creates a new list with all the unique elements of both the given lists. You need to make sure that there are no duplicates in the resulting list. Finally, print the updated list.

Hint: You may create a third list to store the results. You can use membership operators (in, not in) to make sure no duplicates are added.

===================================================================

Output for the above two lists: [1, 2, 4, 5, 7, 99, 200, 303, 70, 3, 500, -5]"""

list_one = [1,2,2,4,5,5,7,99,200,303,70]
list_two = [1,1,2,3,3,3,4,5,200,500,-5]
new_list = list_one + list_two
no_dup_list = []
for i in new_list:
    if i not in no_dup_list:
        no_dup_list.append(i)

print(no_dup_list)