# Author: PCL 11/10/22

#creating a list variable for testing the code
numbers = [7,13,3,8,25,1,0,22]

#creating an if statement that checks if the list has at least 2 or more numbers
#if no, the code prints the error message and stops, if yes it moves on
if(len(numbers) <= 1):
    print("error: list does not meet specifications")
#sorting the list from the lowest to highest number and printing the first and last numbers in the list respectively to lowest and highest
else:
    numbers.sort()
    print("The lowest value is "+str(numbers[0])+", and the highest value is "+str(numbers[len(numbers)-1])+".")

