# Author: PCL 10/28/22

#creating list with 2 names of people in my row and printing it
my_row = ["joe","richie"]
print(my_row)

#replacing the last name in the my_row list with my own name and printing it
my_row[1] = "preston"
print(my_row)

#creating a new list, my_row2, and setting it equal to the my_row list - and printing it
my_row2 = my_row
print(my_row2)

#removing the first name from the my_row list and printing it
del my_row[0]
print(my_row)
#the only name left in the my_row list is my own name which now has the starting index[0]