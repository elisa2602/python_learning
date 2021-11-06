"""
Write a program that iterates over a list of cities
and prints the string 'City: city_name'.

Example
in: cities = ['Rome','London']
out:
    City: Rome
    City: London
"""

cities = ['Rome','London']
count = 0

'''for city_name in cities:
    print('City:' + city_name)'''

while count<len(cities):
    city_name = cities[count]
    print('City: ' + city_name)
    count += 1





 
    


