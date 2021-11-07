"""
Write a program that iterates over a list and count its element.
iteration must be performed with for approach. len() function is not
allowed ;D

Example:
in: data = [1,'b',12.5]
out: 3
"""

data = [1,'b',12.5]
count = 0

for n in data:
    count += 1

print(count)

'''while count<len(data):
    print(data[count])
    count += 1'''
    

