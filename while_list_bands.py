"""
You have 2 lists. One that contains some bands name, the other is empty. Write a program
that removes a band name from the first list if it is not 'Queen' and stores it in the second.

Example:

list1 = ['Metallica','Iron Maiden', 'Queen]'
list2 = []

After execution:

list1 = ['Queen']
list2 = ['Metallica','Iron Maiden']


TIP: you cannot do it with for loops ;D
"""

list1 = ['Mettallica','Iron Maiden','Queen']
list2 = []
listaTemp = []
count = 0

while len(list1) > count :      
    if list1[count] == 'Queen':
        listaTemp.append(list1[count])
    else:
        list2.append(list1[count])
    count += 1

list1 = listaTemp
print(list1)
print(list2) 
    
