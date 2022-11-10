# Author: PCL 11/10/22

#asking the user for 3 numerical inputs
num1 = input("please input a number: ")
num2 = input("please input another number: ")
num3 = input("please input a third number: ")

#creating a list of the inputs in the order they were given and converting them to integers
nums = [int(num1),int(num2),int(num3)]

#checking if the numbers in the list are all even or all odd by seeing what they result in,
#after %2 which will result in 0 if it is even or 1 if it is odd -
#if it is neither all even or all odd results will print mixed
if(nums[0]%2 == 0 and nums[1]%2 == 0 and nums[2]%2 == 0):
    print("even")
elif(nums[0]%2 == 1 and nums[1]%2 == 1 and nums[2]%2 == 1):
    print("odd")
else:
    print("mixed")