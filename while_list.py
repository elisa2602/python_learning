old_list =[1,2,3]
new_list = []
count = 0

'''for element in old_list:
    temp = element + 1
    new_list.append(temp)'''

# while the number of elements<3 : add 1 to every element
while count<len(old_list):
    temp = old_list[count] + 1
    new_list.append(temp)
    count += 1
    

print(new_list)
