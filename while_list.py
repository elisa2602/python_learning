"""Write a program that iterates on a list of number,
and adds 1 to the numbers contained in such list.
The result must be stored in a new list. Iteration must be performed
with while.

Example:
in: original_list = [1,2,3]
out: result_list = [2,3,4]"""

old_list =[1,2,3]
new_list = []
count = 0

while count<len(old_list):
    temp = old_list[count] + 1
    new_list.append(temp)
    count += 1
    

print(new_list)
